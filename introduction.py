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
#Text analyzing, concordance, dispersion, frequency
from nltk.book import *

print(text8.concordance("man"))
print(text8.concordance("woman"))

# print(text8.dispersion_plot(["woman", "lady", "girl"]))