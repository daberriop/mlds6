# /bin/python3
from digitallistening.database.data_manager import *
from digitallistening.preprocessing.dataset_preprocessing import *

def main():
    #Load data
    raw_df = load_raw_data()

    #Execute preprocessin pipeline
    df = process_dataframe(raw_df)
    
    #Save preprocessed data
    export_data_to_parquet(df, "processed_pascual")

if __name__ == "__main__":
    main()
