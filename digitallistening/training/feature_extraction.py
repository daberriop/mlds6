from gensim.models import word2vec
from nltk import WordPunctTokenizer
import numpy as np

def get_tokenized_corpus(corpus):
    tokenizer = WordPunctTokenizer()
    tokenized_clean_text = [tokenizer.tokenize(content) for content in corpus if content]
    return tokenized_clean_text

def get_w2v_model(sentences):
    feature_size = 100 
    window_context = 5 
    min_word_count = 1 
    sample = 1e-3
    epochs = 100


    w2v_model = word2vec.Word2Vec(
            sentences,
            vector_size=feature_size,
            window=window_context,
            min_count=min_word_count,
            sample=sample,
            epochs=epochs
            )

    return w2v_model

def get_w2v_repr(corpus, model):
    w2v_representations = []
    for sentence in corpus:
        try:
            w2v_representations.append(model.wv[sentence].mean(axis=0))
        except:
            w2v_representations.append(np.zeros(shape=(model.vector_size,)))
    return np.array(w2v_representations)

class MeanEmbeddingVectorizer(object):
    def __init__(self,training_sentences):
        tokenized_sentences = get_tokenized_corpus(training_sentences)
        self.w2v_model = get_w2v_model(tokenized_sentences)

    def fit(self, X, y):
        return self

    def transform(self, X):
        tokenized_sentences = get_tokenized_corpus(X)
        return get_w2v_repr(tokenized_sentences, self.w2v_model)


