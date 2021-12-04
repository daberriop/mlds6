#/bin/python3

import gdown 
import os
import dotenv

dotenv.load_dotenv()

fileid = os.getenv('RAW_DATA_FILE_ID')
output = os.getenv('RAW_DATA_OUTPUT')

gdown.download(
        id = fileid,
        output=output
        )
