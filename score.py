import math
def f2_score(precision, recall):
    if precision + recall == 0:
        return 0.0
    return (1 + 2**2) * (precision * recall) / (2**2 * precision + recall)

def eva_f2(top_k, relevant_docs):
    top_k_set = set(top_k)
    relevant_set = set(relevant_docs)
    true_positives = len(top_k_set & relevant_set)

    precision = true_positives / len(top_k) if len(top_k) > 0 else 0
    recall = true_positives / len(relevant_set) if len(relevant_set) > 0 else 0
    f2 = f2_score(precision, recall)

    return precision, recall, f2

top_k = [
    'trường đại học giao thông vận tải là trường đại học mà tôi theo học',
    'tôi muốn thành thạo hai thứ tiếng là tiếng anh và tiếng nhật',
    'Tôi muốn làm siêu nhân',
    'Trường đại học giao thông vận tải'
]

relevant_docs = [
    'trường đại học giao thông vận tải'
]
if __name__ == "__main__":
    print (f'F2 Score : {eva_f2(top_k,relevant_docs)}')