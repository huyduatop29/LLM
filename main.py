import os
import re

from unstructured.partition.auto import partition
from unstructured.chunking.basic import chunk_elements
from unstructured.chunking.title import chunk_by_title
from unstructured.chunking.base import ChunkingOptions
from unstructured.chunking.base import PreChunker

from unstructured.cleaners.core import (
    clean_ordered_bullets,
    group_broken_paragraphs,
    clean_prefix
)
from unstructured.documents.elements import NarrativeText, ElementMetadata

import chromadb
from chromadb.utils import embedding_functions
import torch
from preprocess import preprocessing


folder_path = "E:/Download/DataTest/test"
sentence_tranformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="dangvantuan/vietnamese-embedding")
    # keepitreal/vietnamese-sbert
    # dangvantuan/vietnamese-embedding

chromadb_client = chromadb.PersistentClient(path="vector_database")

collection = chromadb_client.create_collection(
    name="new_collection", 
    embedding_function=sentence_tranformer_ef, 
    metadata = {
        "hnsw:space": "cosine",
        "hnsw:construction_ef": 200,
        "hnsw:M": 16,
        "hnsw:search_ef": 50,
        "hnsw:num_threads": 1,
        "hnsw:resize_factor": 1.2,
        "hnsw:batch_size": 1000,
        "hnsw:sync_threshold": 1000,    
    }
)


id_counter = 1



for filename in os.listdir(folder_path):
    filepath = os.path.join(folder_path, filename)
    cleaned_elements = []
    #chunks =  []

    elements = partition(
        filename=filepath, 
        strategy="fast", 
        max_partition=1000, 
        languages=["eng", "vie"],
        split_pdf_page=True, 
        split_pdf_allow_failed=True, 
        split_pdf_concurrency_level=15
    )   


    text_elements = [el for el in elements if getattr(el, 'category', None) != 'Footer' and 'Header' ]

    for el in text_elements:
        r'''
        cleaned_text = el.text
        cleaned_text = clean_ordered_bullets(cleaned_text)
        cleaned_text = group_broken_paragraphs(cleaned_text)  
        cleaned_text = cleaned_text.lower()
        pattern = r'[\/\\\[\]\{\}\-_():;]'
        cleaned_text = re.sub(pattern, '', cleaned_text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
        cleaned_text = cleaned_text.strip()
        '''
        cleaned_text = el.text
        cleaned_text = preprocessing(cleaned_text)
        

        if len(cleaned_text) > 10:
            metadata = el.metadata if el.metadata else ElementMetadata()
            metadata.page_number = getattr(el.metadata, "page_number", None)
            cleaned_elements.append(
                NarrativeText(cleaned_text, metadata=metadata)
            )
    
    chunks = chunk_elements(cleaned_elements,max_characters= 200, new_after_n_chars= 180, overlap= True)
    print(len(chunks))
    

    documents = []
    metadatas = []
    ids = []

    for i,chunk in enumerate(chunks):
        # page_number = chunk.metadata.page_number if chunk.metadata else None
        page_number = chunk.metadata.page_number if chunk.metadata and chunk.metadata.page_number is not None else "unknown"

        #print (f'chunk{i} - file name {filename} - page number {page_number}: {chunk}')
        #print('\n')

        documents.append(chunk.text)
        metadatas.append({
            "chunk_id": str(id_counter),
            "filename": filename,
            "page_number": page_number,
        })
        ids.append(str(id_counter))
        id_counter += 1

    if documents and metadatas and ids:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids,
        )

        print(f'{filename} added to ChromaDB successfully!')
    else:
        print(f'{filename} skipped because empty!')

print('Update successfully!')


