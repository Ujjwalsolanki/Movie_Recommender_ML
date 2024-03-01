import os
from pathlib import Path
import pandas as pd
import numpy as np
import ast

from logger import logging
from src.utils.common import Common



class DataTransformation:

    def initiate_data_transformation(self):
        try:
            common = Common()
            path = os.path.join('artifacts/')
            file_name = 'validated_movies.csv'

            movies  = common.get_data(path, file_name)
            movies['genres'] = movies['genres'].apply(self.convert)
            movies['keywords'] = movies['keywords'].apply(self.convert)
            movies['cast'] = movies['cast'].apply(self.convert3)
            movies['crew'] = movies['crew'].apply(self.get_director)
            movies['overview'] = movies['overview'].apply(lambda x:x.split())

            movies['cast'] = movies['cast'].apply(self.remove_spaces)
            movies['crew'] = movies['crew'].apply(self.remove_spaces)
            movies['genres'] = movies['genres'].apply(self.remove_spaces)
            movies['keywords'] = movies['keywords'].apply(self.remove_spaces)

            movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
            movies.drop(columns=['overview','genres','keywords','cast','crew'], inplace=True)

            movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))

            common.save_csv(path, file_name, movies) #pd.to_csv('artifacts/validated_movies.csv')

        except Exception as e:
            logging.exception(e)
            raise e

    def convert(self, obj):
        list = []
        for item in ast.literal_eval(obj):
            list.append(item['name'])
        return list
    
    def convert3(self, obj):
        counter = 0
        list = []
        for item in ast.literal_eval(obj):
            if counter != 3:
                list.append(item['name'])
                counter += 1
            else:
                break
        return list
    
    def get_director(self, obj):
        list = []
        for item in ast.literal_eval(obj):
            if item['job'] == 'Director':
                list.append(item['name'])
                break        
        return list
    
    def remove_spaces(self, list):
        data = []
        for item in list:
            data.append(item.replace(" ",""))
        return data