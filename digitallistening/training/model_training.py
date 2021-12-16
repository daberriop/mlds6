from digitallistening.training.feature_extraction import *
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
import pickle
import os
import dotenv

def get_KMeans_model(k:int) -> KMeans:
    return KMeans(n_clusters=k)

def train_KMeans_model(data:list, k,save=True):
    
    pipe = Pipeline([
        ('vectorizer',MeanEmbeddingVectorizer(data)),
        ('model',get_KMeans_model(k))
        ])

    pipe.fit(data)
    if save == True:
        dotenv.load_dotenv()
        file = os.path.join(os.getenv("MODEL_PATH"),f"{os.getenv('MODEL_NAME')}.pkl")
        pickle.dump(pipe, open(file,"wb"))

