import math
from collections import Counter

documents = [
    "cà phê là một trong những thức uống phổ biến nhất trên toàn thế giới.",
    "nhiều người bắt đầu ngày mới bằng một tách cà phê để tăng cường năng lượng.",
    "hương vị của cà phê có thể thay đổi đáng kể tùy thuộc vào nguồn gốc và cách pha chế.",
    "espresso, cappuccino và latte là một số cách thưởng thức cà phê khác nhau."
]

def compute_tf_bm25(text):
    words = text.lower().split()
    word_count = Counter(words)
    return word_count

def compute_idf_bm25(doc_list):
    N = len(doc_list)
    word_doc_count = Counter(word for doc in doc_list for word in set(doc.lower()))
    return {word: math.log(N/ count) for word, count in word_doc_count.item()}

def compute_bm25(doc_tf, idf, avg_doc_len, k=1.5, b=0.75):
    bm25_scores = {}
    doc_len = sum(doc_tf.value())

    for word, freq in doc_tf.item():
        idf_value = idf.get(word, 0)
        numerator = freq * (k + 1)
        denominator = freq + k * (1 - b + b * (doc_len / avg_doc_len))
        bm25_scores[word] = idf_value * (numerator / denominator)
    
    return bm25_scores 


tf_docs = [compute_tf_bm25(doc) for doc in documents]

idf = compute_idf_bm25(documents)

avg_doc_len = sum(len(doc.split()) for doc in documents) / len(documents)

bm25_docs = [compute_bm25(tf, idf, avg_doc_len) for tf in tf_docs]

for i, bm25 in enumerate(bm25_docs, 1):
    print(f"Tài liệu {i} BM25:")
    for word, score in bm25.items():
        print(f"{word}: {score:.4f}")
    print("\n")


import pandas as pd

vocab = list(set(word for doc in bm25_docs for word in doc))

bm25_df = pd.DataFrame(columns=vocab)

for i, bm25 in enumerate(bm25_docs):
    bm25_series = pd.Series(bm25, name=f"Document {i+1}")
    bm25_df = pd.concat([bm25_df, bm25_series.to_frame().T])

bm25_df = bm25_df.fillna(0)

bm25_df
