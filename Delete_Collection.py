import chromadb

# Khởi tạo client
chromadb_client = chromadb.PersistentClient(path="vector_database")

# Xóa collection theo tên
collection_name = "new_collection"
chromadb_client.delete_collection(name=collection_name)

print(f"Collection '{collection_name}' đã được xóa thành công.")
