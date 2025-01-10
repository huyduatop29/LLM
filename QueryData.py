import chromadb
from chromadb.utils import embedding_functions

sentence_tranformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="dangvantuan/vietnamese-embedding")
chromadb_client = chromadb.PersistentClient(path="vector_database")
collection = chromadb_client.get_collection(
    name="new_collection",
    embedding_function= sentence_tranformer_ef,
    )


results = collection.query(
   query_texts='trường đại học giao thông vận tải có trong những tài liệu nào', 
   n_results= 4,
   include=['documents','distances','metadatas'],
)

print(results)
print(collection.count())



for i in range(1407,1410, 1):
    batch = collection.get(
        include=["documents","metadatas"],
        limit=1,
        offset=i)
    print(batch) 


