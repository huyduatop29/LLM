import os
from unstructured.partition.auto import partition
from unstructured.chunking.basic import chunk_elements
from unstructured.chunking.title import chunk_by_title
from Chroma_ver2 import to_chromadb
from unstructured.cleaners.core import (
    clean_ordered_bullets,
    group_broken_paragraphs,
    clean_prefix,
)
from unstructured.documents.elements import NarrativeText


def process_folder(folder_path, chunking_strategy="basic"):
    id_counter = 1
    for filename in os.listdir(folder_path):
        print(filename)
        filepath = os.path.join(folder_path, filename)
        elements = partition(filename=filepath)

        text_elements = [el for el in elements if isinstance(el, NarrativeText)]

        cleaned_text = [clean_prefix(el.text, r"câu ", ignore_case=True) for el in text_elements]
        cleaned_text = [clean_ordered_bullets(el) for el in cleaned_text]
        cleaned_text = [group_broken_paragraphs(el) for el in cleaned_text]

        cleaned_elements = [NarrativeText(text) for text in cleaned_text]
        if chunking_strategy == "title":
            chunks = chunk_by_title(cleaned_elements) 
            to_chromadb(chunks,id_counter)
            id_counter += 1
        else:
            chunks = chunk_elements(cleaned_elements)
            to_chromadb(chunks,id_counter)
            id_counter += 1

def main():
    folder_path = "E:/Download/DataTest/test"
    chunking_strategy = "title"
    chunks = process_folder(folder_path, chunking_strategy)
    # Printing chunks (you can customize this further)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:")
        print(f"  Text: {chunk.text if hasattr(chunk, 'text') else chunk}")
        print(f"  Length: {len(chunk.text) if hasattr(chunk, 'text') else len(str(chunk))} characters")
        print("\n" + "-"*80)


        
if __name__ == "__main__":
    main()
