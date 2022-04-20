from tika import parser
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from string import punctuation
import re

def most_common():
  # Pega o texto contido no PDF e transforma em string
  parsed_pdf = str(parser.from_file("scripts/48500.006904-2019-52.pdf")['content'])
  # Encontra todos os símbolos do texto
  symbol_in_doc = re.findall('[^0-9a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]+',parsed_pdf)
  # Baixa paccotes base da lib 
  nltk.download("popular")
  # Encontra as stopwords do português
  stop_words = set(stopwords.words('portuguese'))
  # Adiciona a lista de stopwords novas palavras
  newStopWords = ('ccee','n°','nº','pág','anexo','documento')
  stop_words.update(newStopWords)
  # Separa as strings em palavras e
    # remove as stopwords da lista de palavras
    # remove as pontuações
    # remove os symbolos encontrados no PDF
  words = [
    word
    for word in word_tokenize(parsed_pdf)
    if len(word) > 3 and
    not word.isdigit() and
    word.lower() not in stop_words and
    word not in punctuation and
    word not in symbol_in_doc
  ]
  # Conta as palavras mais comuns
  noun_freq = Counter(words)
  common_nouns = noun_freq.most_common(5)
  dct = dict((y, x) for y, x in common_nouns)
  print(dct)
  return dct