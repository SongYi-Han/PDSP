from gensim.models.fasttext import load_facebook_model
from gensim.models.fasttext import load_facebook_vectors

model = load_facebook_vectors('fasttext-wiki-news-subwords-300')
res = model.most_similar('apple', topn=5)
print("==="*100)
print(res)

'''
model = api.load("glove-wiki-gigaword-50")
res = model.most_similar('apple', topn=5)
print("==="*100)
print(res)

model = api.load("fasttext-wiki-news-subwords-300")
res = model.most_similar('apple', topn=5)
print("==="*100)
print(res)
#output : [('apples', 0.8046640753746033), ('pear', 0.6897592544555664), ('peach', 0.6626990437507629), ('fruit', 0.6596963405609131), ('apple-', 0.6546189785003662)]

model = api.load("word2vec-google-news-300")
res = model.most_similar('apple', topn=5)
print("==="*100)
print(res)
#output: [('apples', 0.720359742641449), ('pear', 0.6450697183609009), ('fruit', 0.6410146355628967), ('berry', 0.6302295327186584), ('pears', 0.613396167755127)]
'''

