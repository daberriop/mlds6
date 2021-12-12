import os
import re
import dotenv
import pandas as pd

from pandas import DataFrame

def drop_by_language(df:DataFrame) -> DataFrame:
    '''
    Elimina filas quu no esten en español

    Parameters
    ----------
    df: DataFrame
        dataframe con datos sin procesar

    Returns
    -------
    df: DataFrame
        dataframe con solo datos en español

    '''
    return df.drop(df[df["LANGUAGE"]!='Spanish'].index)

def drop_by_mediaprovider(df:DataFrame) -> DataFrame:
    '''
    Elimina datos que no sean de TWITTER

    Parameters
    ----------
    df: DataFrame
        dataframe con datos sin procesar

    Returns
    -------
    df: DataFrame
        dataframe con solo datos de twitter


    '''
    return df.drop(df[df["MEDIA_PROVIDER"]!='TWITTER'].index)

def remove_columns(df:DataFrame) -> DataFrame:
    '''
    Elimina columnas que no aportan informacion util para el análisis
    
    Parameters
    ----------
    df: DataFrame
        dataframe con datos sin procesar

    Returns
    -------
    df: DataFrame
        dataframe con solo las columnas relevantes
    '''

    temp_df = df.drop(df.columns[25:], axis=1)
    temp_df.drop(["AUTHOR","HEADLINE","REGION","MEDIA_PROVIDER", "ENGAGEMENT","ARTICLE_URL", "EXTERNAL_ID", "INBOUND_LINKS", "FORUM_THREAD_SIZE","LIKES_AND_VOTES","UNIQUE_COMMENTERS","POST_STATUS","LANGUAGE","VIEW_COUNT", "COMMENT_COUNT"],axis=1,inplace=True)
    return temp_df

def fillna_post_type(df:DataFrame) -> DataFrame:
    '''
    Llena los datos nulos de la variable POST_TYPE

    Parameters
    ----------
    df: DataFrame
        dataframe con datos sin procesar

    Returns
    -------
    df: DataFrame
        dataframe sin elementos nulos para la variable POST_TYPE
 
    '''
    return df.fillna(value={"POST_TYPE":"TWEET"})


def get_retweet_count(tweet:str, retweet_counts:DataFrame)->int:
    '''
    Retorna el numero de veces que un tweet fue retwiteado

    Parameters
    ----------
    tweet: str
        el contenido del tweet para saber la cantidad de retweets
    retweet_counts: DataFrame
        dataframe con la informccion de conteos por tweet

    Returns
    -------
    count : int
        el valor numero de la cantidad de retweets

    '''
    if tweet in retweet_counts.index:
        return retweet_counts.loc[tweet]["POST_TYPE"]
    else:
        return 0

def add_retweet_counts(df:DataFrame) -> DataFrame:
    '''
    Añade el conteo de retwwts al dataframe

    Parameters
    ----------
    df: DataFrame
        dataframe con datos sin procesar

    Returns
    -------
    df: DataFrame
        dataframe con conteos de retweets

    '''
    retweet_counts = df[df["POST_TYPE"] == "RETWEET"].groupby("CONTENT").count()
    df_temp = df.copy()
    df_temp.drop_duplicates(subset=['CONTENT'], inplace=True)
    df_temp["RETWEET_COUNTS"] = df_temp["CONTENT"].apply(lambda x: get_retweet_count(x, retweet_counts))
    return df_temp

def process_dataframe(raw_df: DataFrame)->DataFrame:
    '''
    Run process pipeline

    Parameters
    ----------
    raw_df: DataFrame
        data frame con datos originales

    Returns
    -------
    processed_df: DataFrame 
        dataframe procesado

    '''
    processed_df = (
            raw_df
            .pipe(drop_by_language)
            .pipe(drop_by_mediaprovider)
            .pipe(remove_columns)
            .pipe(fillna_post_type)
            .pipe(add_retweet_counts)
            )
    processed_df["PUBLISH_DATE"]= pd.to_datetime(processed_df["PUBLISH_DATE"])
    processed_df["HARVESTED_DATE"]= pd.to_datetime(processed_df["HARVESTED_DATE"])
    processed_df = processed_df.convert_dtypes()
    return processed_df
