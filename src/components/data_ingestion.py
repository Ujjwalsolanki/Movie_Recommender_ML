import os
from pathlib import Path
import pandas as pd
import numpy as np

from logger import logging
from src.utils.common import Common

class DataIngestion:

    def initiate_data_ingestion(self):
        try:
            common = Common()

            path = os.path.join('training_files/')
            movies_csv = 'tmdb_5000_movies.csv'
            credits_csv = 'tmdb_5000_credits.csv'
            movies = common.get_data(path, movies_csv)
            credits = common.get_data(path, credits_csv)

            movies = movies.merge(credits, on='title')

            movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

            movies.dropna(inplace=True)

            validate_files_path = os.path.join('artifacts/')
            file_name = 'validated_movies.csv'
            common.save_csv(validate_files_path, file_name, movies)


        except Exception as e:
            logging.exception(e)
            raise e