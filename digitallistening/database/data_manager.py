import pandas as pd
import os
import dotenv

from pandas import DataFrame

def load_raw_data() -> DataFrame:
    '''
    Realiza la carga de los datos raw en un Dataframe

    Returns
    -------
    rawdata_df: DataFrame
        Dataframe con los datos sin procesar

    '''

    dotenv.load_dotenv()
    rawdata_path = os.getenv("RAW_DATA_OUTPUT")
    rawdata_df = pd.read_csv(rawdata_path)
    return rawdata_df


def export_data_to_parquet(data:DataFrame):
    '''
    Exporta datos a formato parquet
    Parameters
    ----------
    data: DataFrame
        The dataframe to save
    file_name: str
        The name of the file to export

    '''
    dotenv.load_dotenv()
    data_path = os.getenv("DATA_PATH")
    file_name = os.getenv("PROCESSED_DATA_FILE_NAME")
    file = f"{file_name}.parquet"
    file_path = os.path.join(data_path,file)
    data.to_parquet(file_path)

def load_data_from_parquet():
    dotenv.load_dotenv()
    data_path = os.getenv("DATA_PATH")
    file_name = os.getenv("PROCESSED_DATA_FILE_NAME")
    file = f"{file_name}.parquet"
    file_path = os.path.join(data_path,file)
    dataset = pd.read_parquet(file_path)
    return dataset
