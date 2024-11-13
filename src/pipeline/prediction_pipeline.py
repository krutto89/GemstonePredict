import os
import sys
import pandas as pd
from src.exception.exception import CustomException
from src.logger.logger_example import logger_example
from src.utils.utils import load_object


class PredictPipeline:
    # def __new__(self):
    #     print("Predict pipeline")
    def __init__(self):
        print("Predict pipeline")

    def predict(self,features):
        try:
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            model_path = os.path.join('artifacts','model.pkl')

            preprocessor = load_object(file_path=preprocessor_path)
            model = load_object(file_path=model_path)

            data_scaled = preprocessor.transform(features)

            prediction = model.predict(data_scaled)

            return prediction

        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self):
        pass
    def get_data_as_dataframe(self):
        pass


        