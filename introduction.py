#Tokenizing
from nltk.tokenize import sent_tokenize, word_tokenize

exemplo = "O clássico solteiro versus casados do bairro Maria Aparecida Pedrossian já tem mais de 30 anos e a rapaziada vestida de mulher na lama nunca decepciona na resenha. Triste para a turma de aliança no dedo que foi goleada e assume que esse ano é da galera de carreira solo."

print(sent_tokenize(exemplo)) #Tokenize by sentence
print(word_tokenize(exemplo)) #Tokenize by word
#-------------------------
print("\n")
#-------------------------
#Filtering stopwords
from nltk.corpus import stopwords

palavrasExemplo = word_tokenize(exemplo)
stopWords = set(stopwords.words("portuguese"))
filtrado = [ palavra for palavra in palavrasExemplo if palavra.casefold() not in stopWords]

print(filtrado)
#-------------------------
print("\n")
#-------------------------
#Stemming
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stemmedWords = [stemmer.stem(word) for word in filtrado]
print(stemmedWords)
#-------------------------
print("\n")
#-------------------------
#Lemmatizing
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("scarves"))
#-------------------------
print("\n")
#-------------------------
#POS Tagging
from nltk import pos_tag

quote = "If you wish to make an apple pie from scratch, you must first invent the universe."
wordsQuote = word_tokenize(quote)

print(pos_tag(wordsQuote))
#-------------------------
print("\n")
#-------------------------
#Chunking
from nltk import RegexpParser

tagged_quote = pos_tag(wordsQuote)
grammar = "NP: {<DT>?<JJ>*<NN>}" #Noun phrase chunking
chunk = RegexpParser(grammar)

tree = chunk.parse(tagged_quote)
tree.draw()
#-------------------------
print("\n")
#-------------------------
#Text analyzing, concordance
from nltk.book import *

print(text8.concordance("man"))
print(text8.concordance("woman"))
#-------------------------
print("\n")
#-------------------------
#Dispersion and frequency
from nltk import FreqDist

text8.dispersion_plot(["woman", "lady", "girl", "gal", "man", "gentleman", "boy", "guy"]) 

frequency_distribution = FreqDist(text8)
print(frequency_distribution)
print(frequency_distribution.most_common(20))