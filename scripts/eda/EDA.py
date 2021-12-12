# -*- coding: utf-8 -*-
# # Análisis exploratorio de datos
#
#

# ## **1. Importación de librerías**

import emoji
import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import re
import pandas as pd
import numpy as np
from wordcloud import WordCloud
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import metrics 
import matplotlib.pyplot as plt 
import seaborn as sns
from gensim.models import word2vec
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.cluster import KMeans

plt.style.use("ggplot")
nltk.download("popular")
plt.style.use("ggplot")
np.random.seed(0)

# ### **a. Recolección inicial de datos**
#
# Se trabajará con el conjunto de datos de los registros de los posts en tweeter de los últimos dos meses obtenidos por nuestro software de escucha digital.
#

col_list=['AUTHOR','CONTENT','PUBLISH_DATE']

pascual= pd.read_csv('pascual.csv',usecols=col_list)
pascual

# Se plantea un primer acercamiento para establecer el sentimiento (Positivo, Negativo o Neutro) de los posts basados en Vader

analyzer = SentimentIntensityAnalyzer()

post=pascual['CONTENT'].tolist()

post[0]

sentimiento= ([analyzer.polarity_scores(sentence) for sentence in post])
sentimiento= [list(sentence.values()) for sentence in sentimiento]

analyzer.polarity_scores(post[1]).keys()

pascual["vader"]=sentimiento
vader_split= pd.DataFrame(pascual['vader'].tolist(),columns=['NEG','NEU','POS','COMP'])
pascual= pd.concat([pascual,vader_split], axis=1)
pascual = pascual.drop('vader', axis= 1)
pascual.index = [x for x in range(0, len(pascual.values))]
pascual.index.name='id'
pascual
#pascual= pascual.vader.apply(pd.Series)

conds= [pascual["COMP"]>=0.05,
        (pascual["COMP"] > -0.05)&(pascual["COMP"] < 0.05),
        pascual["COMP"]<=-0.05]
choices= ['Positive','Neutral','Negative']

pascual['COMP']=np.select(conds,choices).tolist()

val_pascual= pascual[['COMP']]

# ### **b. Procesamiento, exploración y limpieza de los datos**
#

tweets= pascual['CONTENT'].tolist()

wpt = WordPunctTokenizer()
sw = stopwords.words("spanish")


def preprocessing(doc):
    # Escriba su código aquí
    doc = re.sub('@[^\s]+','',doc) #eliminaremos los usernames de los tweets
    doc= re.sub('https:[^\s]+','',doc) #eliminaremos las url en los tweets
    doc = emoji.get_emoji_regexp().sub(u'', doc) #eliminaremos los emojis
    doc = re.sub(r'[^a-zA-Z\s]', '', doc)
    doc = doc.lower()

    return " ".join(
            token
            for token in wpt.tokenize(doc)
            if (
                len(token)>=2 and
                token not in sw)
            )
norm_corpus=list(map(preprocessing,tweets))

# ### **c. Entendimiento de los datos**

# +
wc= WordCloud(stopwords=sw,
                width= 1600,
                height=800).generate_from_text(' '.join(norm_corpus))

fig, ax= plt.subplots(1, 1, figsize=(20,10))
ax.imshow(
    wc,
    interpolation='bilinear'
      )
ax.axis("off")
# -
tokenized_corpus = [
        [token for token in wpt.tokenize(doc) if token not in sw] for doc in norm_corpus
        ]
tokenized_corpus[3:5]

vacios=[i for i,x in enumerate(tokenized_corpus) if not x]

pascual=pascual.drop(index=vacios)

tokenized_corpus1= [x for x in tokenized_corpus if x]
print(len(tokenized_corpus))
print(len(tokenized_corpus1))

texto=[]
for sentence in tokenized_corpus1:
  texto= texto + sentence
texto=' '.join(texto)


tokens= wpt.tokenize(texto)
tokens[:5]

freq_dist = nltk.FreqDist(tokens)
print(freq_dist)

# +
words, counts = (freq_dist.keys(), freq_dist.values())

ordered_freqs = pd.DataFrame(
        sorted(
            zip(words, counts),
            key=lambda x: x[1],
            reverse=True
            ),
        columns=["word", "count"]
        )
ordered_freqs

# +

SnowballStemmer.languages
sst = SnowballStemmer(language="spanish")
stemmer_snow=[]
for i in range(len(tokens)):
  word=sst.stem(tokens[i])
  stemmer_snow.append(word)
print(stemmer_snow) 
len(stemmer_snow)

# -

freq_dist_snow = nltk.FreqDist(stemmer_snow)
print(freq_dist_snow)

# +
words_snow, counts_snow = (freq_dist_snow.keys(), freq_dist_snow.values())

ordered_freqs_snow = pd.DataFrame(
        sorted(
            zip(words_snow, counts_snow),
            key=lambda x: x[1],
            reverse=True
            ),
        columns=["word", "count"]
        )
ordered_freqs_snow[:10]

# +
wc= WordCloud(stopwords=sw,
                width= 1600,
                height=800).generate_from_text(' '.join(stemmer_snow))

fig, ax= plt.subplots(1, 1, figsize=(20,10))
ax.imshow(
    wc,
    interpolation='bilinear'
      )
ax.axis("off")
# -








