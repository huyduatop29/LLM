'''
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

text = 'a) Tham dự thầu với tư cách là nhà thầu đối với gói thầu do mình làm bên mời thầu, chủ đầu tư hoặc thực hiện nhiệm vụ của bên mời thầu, chủ đầu tư không đúng quy định của Luật Đấu thầu; b) Tham gia lập, đồng thời tham gia thẩm định E-HSMT đối với cùng một gói thầu; c) Tham gia đánh giá E-HSDT đồng thời tham gia thẩm định kết quả lựa chọn nhà thầu đối với cùng một gói thầu; '

print(preprocessing(text))

'''

from collections import Counter, defaultdict
import string

letters = set('aáàảãạăaáàảãạăắằẳẵặâấầẩẫậbcdđeéèẻẽẹêếềểễệfghiíìỉĩịjklmnoóòỏõọôốồổỗộơớờởỡợpqrstuúùủũụưứừửữựvwxyýỳỷỹỵz0123456789')

def clean_word(w):
    new_w = ''
    for letter in w:
        if letter.lower() in letters or letter == '.':
            new_w += letter.lower()
    return new_w

def preprocessing(doc):
    doc = doc.replace('\n', ' ').replace('==', ' ')
    words = doc.split()
    cleaned_words = [clean_word(word) for word in words]
    new_doc = ' '.join(cleaned_words)
    return new_doc

#text = 'a) Tham dự thầu với tư cách là nhà thầu đối với gói thầu do mình làm bên mời thầu, chủ đầu tư hoặc thực hiện nhiệm vụ của bên mời thầu, chủ đầu tư không đúng quy định của Luật Đấu thầu; b) Tham gia lập, đồng thời tham gia thẩm định E-HSMT đối với cùng một gói thầu; c) Tham gia đánh giá E-HSDT đồng thời tham gia thẩm định kết quả lựa chọn nhà thầu đối với cùng một gói thầu; '

#print(preprocessing(text))
