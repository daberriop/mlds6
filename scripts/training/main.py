#/bin/python3
from digitallistening.training.feature_extraction import *
from digitallistening.training.model_training import *
from digitallistening.database.data_manager import *
def main():
    # load preprocessed data

    data = load_data_from_parquet()
    
    corpus = data["CONTENT_CLEAN"]
    
    # train and save model

    train_KMeans_model(corpus, 9)



if __name__ == "__main__":
    main()

