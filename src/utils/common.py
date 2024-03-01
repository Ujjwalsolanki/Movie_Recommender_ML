import pandas as pd
from pathlib import Path
from logger import logging

class Common:

    def get_data(self, path:Path, file_name:str)->pd.DataFrame:
        try:
            csv = pd.read_csv(path + file_name)
            return csv
        except OSError as e:
            logging.exception("OS error")
            logging.exception(e)
            raise e
        except Exception as e:
            logging.exception(e)
            raise e
        
    def save_csv(self, path:Path, file_name:str, data:pd.DataFrame):
        try:
            data.to_csv(path + file_name, index=False)
        except OSError as e:
            logging.exception("OS error")
            logging.exception(e)
            raise e
        except Exception as e:
            logging.exception(e)
            raise e