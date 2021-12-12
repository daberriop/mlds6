# -*- coding: utf-8 -*-
# # Mejora Escucha digital 

import os
import dotenv
import pandas as pd
import re
import nltk
import pprint

dotenv.load_dotenv()

rawdata = os.getenv("RAW_DATA_OUTPUT")
rawdata

rawdata_df = pd.read_csv(rawdata)

pprint.pprint(rawdata_df.info())

rawdata_df.head()

rawdata_df["LANGUAGE"].unique()

rawdata_df.drop(rawdata_df[rawdata_df["LANGUAGE"]!='Spanish'].index, inplace=True)
rawdata_df.drop(rawdata_df.columns[25:],axis=1,inplace=True)

rawdata_df.info()

rawdata_df["MEDIA_PROVIDER"].unique()

rawdata_df.drop(rawdata_df[rawdata_df["MEDIA_PROVIDER"]!='TWITTER'].index, inplace=True)

rawdata_df["REGION"].unique()

rawdata_df.drop(["AUTHOR","HEADLINE","REGION","MEDIA_PROVIDER", "ENGAGEMENT", "ARTICLE_URL", "EXTERNAL_ID", "INBOUND_LINKS", "FORUM_THREAD_SIZE", "LIKES_AND_VOTES","UNIQUE_COMMENTERS","POST_STATUS","LANGUAGE", "VIEW_COUNT", "COMMENT_COUNT"],axis=1,inplace=True)

rawdata_df.info()

rawdata_df.fillna(value={"POST_TYPE":"TWEET"},inplace=True)

rawdata_df_temp =rawdata_df.loc[:,["CONTENT","POST_TYPE"]]
rawdata_df_temp

rawdata_df_temp.loc[273]["CONTENT"]

rawdata_df_temp.loc[274]["CONTENT"]

rawdata_df_temp[rawdata_df_temp["POST_TYPE"] == "RETWEET"]

retweet_count = rawdata_df_temp[rawdata_df_temp["POST_TYPE"] == "RETWEET"].groupby("CONTENT").count()

retweet_count

retweet_count["POST_TYPE"].sum()

rawdata_df.drop_duplicates(subset=['CONTENT'], inplace = True)


def get_retweets(x):
    if x in retweet_count.index:
        return retweet_count.loc[x]["POST_TYPE"]
    else:
        return 0


rawdata_df["RETWEET_COUNTS"] = rawdata_df["CONTENT"].apply(get_retweets)

rawdata_df.info()

rawdata_df["RETWEET_COUNTS"].sum()

rawdata_df["PUBLISH_DATE"]= pd.to_datetime(rawdata_df["PUBLISH_DATE"])
rawdata_df["HARVESTED_DATE"]= pd.to_datetime(rawdata_df["HARVESTED_DATE"])

rawdata_df = rawdata_df.convert_dtypes()

rawdata_df.info()

rawdata_df.head()

import emoji


def remove_emojis(text):
    return emoji.get_emoji_regexp().sub('', text) 


def replace_latin(text):
    clean_text = re.sub("[ñ]","n",text)
    clean_text = re.sub("[á]","a",clean_text)
    clean_text = re.sub("[é]","e",clean_text)
    clean_text = re.sub("[í]","i",clean_text)
    clean_text = re.sub("[ó]","o",clean_text)
    clean_text = re.sub("[ú]","u",clean_text)
    return clean_text


def remove_urls(text):
    pattern = r'(https?)(:\/\/)(\S*)'
    return re.sub(pattern,"",text)


def remove_special_characters(text):
    pattern = r'[^a-zA-Z_\s]'
    return re.sub(pattern,'',text)


from nltk import WordPunctTokenizer
from nltk.corpus import stopwords
nltk.download('stopwords')


def remove_stopwords(text):
    sw = stopwords.words('spanish')
    tokenizer = WordPunctTokenizer()
    tokens = tokenizer.tokenize(text)
    clean_tokens = [token for token in tokens if token not in sw and len(token) > 2]
    return " ".join(clean_tokens)



def clean_text(text):
    clean_text = text.lower()
    clean_text = replace_latin(clean_text)
    clean_text = remove_emojis(clean_text)
    clean_text = remove_urls(clean_text)
    clean_text = remove_special_characters(clean_text)
    clean_text = remove_stopwords(clean_text)
    return clean_text



sample_text = rawdata_df["CONTENT"][30]
sample_text

clean_sample_text = clean_text(sample_text)
clean_sample_text 

rawdata_df["CONTENT_CLEAN"] = rawdata_df["CONTENT"].apply(clean_text)

rawdata_df

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# +
norm_corpus = rawdata_df["CONTENT_CLEAN"] 
wc= WordCloud(width= 1600,height=800).generate_from_text(' '.join(norm_corpus))

fig, ax= plt.subplots(1, 1, figsize=(20,10))
ax.imshow(
    wc,
    interpolation='bilinear'
      )
ax.axis("off")
# -

from gensim.models import word2vec
import numpy as np

tokenizer = WordPunctTokenizer()
tokenized_clean_text = [tokenizer.tokenize(content) for content in rawdata_df["CONTENT_CLEAN"] if content]


def get_w2v_repr(corpus): 
    # Parámetros del modelo w2v
    feature_size = 100 
    window_context = 5 
    min_word_count = 1 
    sample = 1e-3
    epochs = 100


    w2v_model = word2vec.Word2Vec(
            tokenized_clean_text,
            vector_size=feature_size,
            window=window_context,
            min_count=min_word_count,
            sample=sample,
            epochs=epochs
            )
    
    w2v_representations = []
    
    for sentence in corpus:
        try:
            w2v_representations.append(w2v_model.wv[sentence].mean(axis=0))
        except:
            w2v_representations.append(np.zeros(shape=(feature_size,)))
    return np.array(w2v_representations)

X_w2v = get_w2v_repr(tokenized_clean_text)

from sklearn.manifold import TSNE


tsne = TSNE(
    n_components=2,
    random_state=0,
    n_iter=1000,
    perplexity=2,
    verbose=1
    )
T = tsne.fit_transform(X_w2v)

plt.figure(figsize=(20, 15))
plt.scatter(T[:, 0], T[:, 1], alpha=0.3)

from sklearn.cluster import KMeans

# +
ks = np.arange(1, 25)

scores = [-KMeans(n_clusters=k).fit(X_w2v).score(X_w2v) for k in ks]
# -

plt.figure(dpi=100, figsize=(8, 4))
plt.plot(ks,scores,"*-")
plt.xlim([ks.min(), ks.max()])
plt.xlabel("$K$")
plt.ylabel("$\mathcal{L}$")

clf_kmeans = KMeans(n_clusters=9,init='k-means++', max_iter=1000 )
clf_kmeans.fit(X_w2v)

clusters = clf_kmeans.predict(X_w2v)
plt.figure(figsize=(20, 15))
plt.scatter(T[:, 0], T[:, 1], c=clusters, alpha=0.4)


