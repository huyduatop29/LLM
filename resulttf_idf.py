import math
from collections import Counter, defaultdict
import string


def rounding(num):
    return math.floor(num * 1000) / 1000

def get_tf(num, doc_length):
    return rounding(num/doc_length)


chunks = [
    'trường đại học giao thông vận tải là trường đại học mà tôi theo học',
    'tôi muốn thành thạo hai thứ tiếng là tiếng anh và tiếng nhật',
    'Tôi muốn làm siêu nhân',
    'Trường đại học giao thông vận tải'
]


def score_tf_idf(chunks):

    stats = {
    "words": defaultdict(set),
    "docs": defaultdict(lambda: defaultdict(int))
    }

    for i,doc in enumerate(chunks):
        if i not in stats['docs']:
            stats['docs'][i] = defaultdict(int)

        for word in doc.split():
            if i not in stats['words']:
                stats['words'][word] = {i}
            else:
                stats['words'][word].add(i)

            stats['docs'][i][word] += 1

    # print (stats['docs'][0])

    words = list(stats['words'].keys())

    idf = defaultdict(float)

    N= len(chunks)

    for word in words:
        df = len(stats['words'][word])
        idf[word] = math.log10(N / df)

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

    q = 'đại học'

    finals = [] 

    for i in range(len(chunks)):
        score = 0

        for t in q.split():
            t = t.lower()
            score += tf_idf_list[t][i] / ds[i]
        finals.append((score, i))

    finals = sorted(finals, key= lambda x: -x[0])
    return finals

'''
def f2_score(precision, recall):
    if precision + recall == 0:
        return 0.0  # Avoid division by zero
    return (1 + 2**2) * (precision * recall) / (2**2 * precision + recall)

# Example usage:
precision = 0.1  # Example precision
recall = 0.1     # Example recall
'''

if __name__ == '__main__':
    finals = score_tf_idf(chunks)
    #print(final[0][1])
    print(finals)


