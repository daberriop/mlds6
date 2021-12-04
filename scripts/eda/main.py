# # Mejora Escucha digital 

import os
import dotenv
import pandas as pd

dotenv.load_dotenv()

rawdata = os.getenv("RAW_DATA_OUTPUT")
rawdata

rawdata_df = pd.read_csv(rawdata)

rawdata_df.info()

rawdata_df.head()

rawdata_df_temp =rawdata_df.loc[:,["CONTENT","POST_TYPE"]]
rawdata_df_temp

rawdata_df_temp.loc[273]["CONTENT"]

rawdata_df_temp.loc[274]["CONTENT"]

rawdata_df_temp[rawdata_df_temp["POST_TYPE"] == "RETWEET"]


