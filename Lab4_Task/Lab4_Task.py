
#from lib2to3.pgen2 import token
from concurrent.futures.process import _system_limited
from ctypes.wintypes import WORD
from multiprocessing.managers import Token
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('omw-1.4')
#print(nltk.__version__)

#text1 = "Hi everybody, I'm Doctor Nick! Mr. Plow, that's my name. That name again is Mr. Plow! Release the hounds!"
#with open (r'C:\Users\User\OneDrive - New Zealand Skills & Education Group\SWD503 - Data Analysis\Lab4_TextAnalysisUsingPython\intro.txt')as f:
    #text1= f.read()
    
with open (r'C:\Users\DJBur\OneDrive - New Zealand Skills & Education Group\SWD503 - Data Analysis\Lab4_TextAnalysisUsingPython\Chapel.txt')as f:
    text1= f.read()
#print("Original text:", text1)

#Sentence Tokenisation
"""
from nltk.tokenize import sent_tokenize

tokenized_sentence= sent_tokenize(text1)
print("Tokenized Sentence:", tokenized_sentence)
"""

#Word Tokenisation

from nltk.tokenize import word_tokenize

tokenized_word= word_tokenize(text1)
print("Tokenized Word:", tokenized_word)
print("\n")

#Frequency distribution
"""
from nltk.probability import FreqDist
Freq1=FreqDist(tokenized_word)
print(Freq1)
print("\n")
print(Freq1.most_common(20)) #prints the top (20) words to list, with number of occurances
print("\n")
"""
#Plotting frequency distribution 
#import matplotlib as plt
#Freq1.plot(20, cumulative=False)
#plt.show

#Stopwords

#Stop words are commonly used words excluded 
#from searches to help index and parse web pages faster. 
#While most Internet search engines and NLP (natural language processing) utilize stop words, 
#they do not prevent users from using them. Instead, the words are only ignored when the search results are displayed.
from nltk.corpus import stopwords
stop_words= set(stopwords.words('english'))
#print("Stopwords:", stop_words)
#print("\n")

#Filtering

filtered_sentence =[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_sentence.append(w)
#print("Filtered Sentence:", filtered_sentence)
#print("\n")

Otherwords= [".", ",", "'","the", "of", "in" , "(", ")", "and", "to", "is", "was", "[", "]" ]
filtered_sentence1=[]
for t in filtered_sentence:
    if t not in Otherwords:
        filtered_sentence1.append(t)
#print("New Filtered Sentence:", filtered_sentence1)
#print("\n")

#Freq2= FreqDist(filtered_sentence1)
#print(Freq1)
#print(Freq2.most_common(10))

#frequency distribution plot
"""
import matplotlib as plt
Freq2.plot(10, cumulative=False)
plt.show
"""
#Stemming

#Shortens the words in the sentence, 'referred' becomes 'refer' etc.
from nltk.stem import PorterStemmer
ps1= PorterStemmer()
stemmedword = ps1.stem("initial")
#print(stemmedword)
#print("\n")

ps2=PorterStemmer()
stemmed_words=[]
for w in filtered_sentence1:
    stemmed_words.append(ps2.stem(w))
print("Stemmed sentence:", stemmed_words)
print("\n")

#Lemmatization 

from nltk.stem.wordnet import WordNetLemmatizer
lem=WordNetLemmatizer()
word= "reticulating"
#print("lemmatized word:", lem.lemmatize(word, pos="n"))

lem_words=[]
for w in filtered_sentence1:
    lem_words.append(lem.lemmatize(w, pos="n"))
print("lemmatized sentence: ", lem_words)
print("\n") 

nltk.download('averaged_perceptron_tagger')
Position_tag = nltk.pos_tag(lem_words)
print(Position_tag) #determines the type and position of the word
