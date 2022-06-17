from concurrent.futures.process import _system_limited
from ctypes.wintypes import WORD
from multiprocessing.managers import Token
import nltk
import pandas as pd
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('omw-1.4')
#print(nltk.__version__)


#,encoding="utf8" (using this encoder to handle the emmojis)
with open (r'C:\Users\User\OneDrive - New Zealand Skills & Education Group\SWD503 - Data Analysis\FridayActivity_22-06-05\DrakeTakeCareRihanna.txt',encoding="utf8") as f:
    text1= f.read()
#print(text1)

#Word Tokenisation

from nltk.tokenize import word_tokenize

tokenized_word= word_tokenize(text1)

#stemming
from nltk.stem import PorterStemmer

ps1= PorterStemmer()
stemmedword = ps1.stem("masterpiece")

ps2=PorterStemmer()
stemmed_words=[]
for w in tokenized_word:
    stemmed_words.append(ps2.stem(w))
#print("Stemmed sentence:", stemmed_words)
#print("\n")

#Stopwords
from nltk.corpus import stopwords
stop_words= set(stopwords.words('english'))

filtered_sentence =[]
for w in stemmed_words:
    if w not in stop_words:
        filtered_sentence.append(w)

Otherwords= [".",",","'","`","the","of","in","(",")","thi","and","to","is","was","[","]","I","'ll","n't","'ve","4","'s","5","1","And","3","2","6","months","month","ago","Year","wa","way","ha","'caus","mani",""]
filtered_sentence1=[]
for t in filtered_sentence:
    if t not in Otherwords:
        filtered_sentence1.append(t)

#frequency distribution plot

from nltk.probability import FreqDist
Freq1= FreqDist(filtered_sentence1)
print(Freq1)
print(Freq1.most_common(30))

import matplotlib as plt
Freq1.plot(20, cumulative=False)
plt.show