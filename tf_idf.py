import math
from collections import Counter, defaultdict
import string

import math

documents = [
    "Quả bưởi ngon",
    "Quả Quả táo dở"
]

letters = set('aáàảãạăaáàảãạăắằẳẵặâấầẩẫậbcdđeéèẻẽẹêếềểễệfghiíìỉĩịjklmnoóòỏõọôốồổỗộơớờởỡợpqrstuúùủũụưứừửữựvwxyýỳỷỹỵz0123456789')

def clean_word(w):
    new_w = ''
    for letter in w:
        if letter.lower() in letters or letter == '.':
            new_w += letter.lower()
    return new_w

def preprocessing(docs):
    new_docs = []
    for doc in docs:
        doc = doc.replace('\n', ' ').replace('==', ' ')
        words = doc.split()
        cleaned_words = [clean_word(word) for word in words]
        new_doc = ' '.join(cleaned_words)
        new_docs.append(new_doc)
    return new_docs

def compute_tf(text):
    words = text.lower().split()
    word_count = Counter(words)
    return {word: count / len(words) for word, count in word_count.items()}

def compute_idf(doc_list):
    word_doc_count = Counter(word for doc in doc_list for word in set(doc.lower().split()))
    total_docs = len(doc_list)
    return {word: math.log(total_docs / count) for word, count in word_doc_count.items()}

def compute_tfidf(tf, idf):
    return {word: tf.get(word, 0) * idf.get(word, 0) for word in tf}

# Sử dụng defaultdict cho stats
stats = {
    "words": defaultdict(set),
    "docs": defaultdict(lambda: defaultdict(int))
}

for i, doc in enumerate(documents):
    for word in doc.split():
        if word not in stats['words']:
            stats['words'][word] = {i}
        else:
            stats['words'][word].add(i)

        stats['docs'][i][word] += 1



def rounding(num):
    return math.floor(num * 1000) / 1000

def get_tf(num, doc_length):
    return rounding(num/doc_length)

words = stats['words'].key()

idf = defaultdict(float)

N = len(documents)

for word in words:
    df = len(stats['words'][word])
    idf[word] = math.log10(N/df)

tf_idf_list = defaultdict(lambda: defaultdict(float))
ds = defaultdict(float)

for doc in stats['docs']:
    d = 0
    for word in words:
        doc_length = sum(stats['docs'][doc].values())
        tf = get_tf(stats['docs'][doc][word], doc_length)

        tf_idf = tf * idf[word]

        d += tf_idf  ** 2
        tf_idf_list[word][doc] = tf_idf
    d_ = d ** (1/2)

    ds[doc] = rounding(d_)


#print(stats['docs'][1])

# Tính TF và IDF
tf_docs = [compute_tf(doc) for doc in documents]
#print(tf_docs)

idf = compute_idf(documents)
#print(idf)
