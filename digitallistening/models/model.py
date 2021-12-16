import pickle
import os
import dotenv
from digitallistening.preprocessing.text_preprocessing import *
from digitallistening.training.feature_extraction import *
def predict(corpus:list):
    dotenv.load_dotenv()
    file = os.path.join(os.getenv("MODEL_PATH"),f"{os.getenv('MODEL_NAME')}.pkl")

    model = pickle.load(open(file,"rb"))
    clean_corpus = [ clean_text(text) for text in corpus]
    return model.predict(clean_corpus)

