import os
from pathlib import Path
import pickle
import pandas as pd
import numpy as np
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


from logger import logging
from src.utils.common import Common



class ModelTrainer:
        

    def initiate_model_training(self):
        try:
            common = Common()
            path = os.path.join('artifacts/')
            file_name = 'validated_movies.csv'

            movies  = common.get_data(path, file_name)
            movies['tags'] = movies['tags'].apply(self.stem)

            cv = CountVectorizer(max_features=5000, stop_words='english')
            vectors = cv.fit_transform(movies['tags']).toarray()

            similarity = cosine_similarity(vectors)

            # pickle.dump(new,open('movie_list.pkl','wb'))
            pickle.dump(similarity,open('artifacts/similarity.pkl','wb'))


        except Exception as e:
            logging.exception(e)
            raise e

    
    def stem(self, text):
        porter_stemmer = PorterStemmer()
        data = []
        for word in text.split():
            data.append(porter_stemmer.stem(word))
        
        return " ".join(data)
    

    # def recommend(movie):
    #     index = df[df['title'] == movie].index[0]
    #     distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    #     for i in distances[1:6]:
    #         print(df.iloc[i[0]].title)