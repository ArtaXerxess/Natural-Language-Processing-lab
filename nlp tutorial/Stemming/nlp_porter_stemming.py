# Porter Stemming
from nltk.stem.porter import PorterStemmer
p = PorterStemmer()
words = ['wharves','symposiums','acetylcysteines','acotyledons']
def porterStemming(words):
    print("Word \t PorterStemmer")
    for word in words:
        print(word," -> ",p.stem(word=word))
porterStemming(words=words)
