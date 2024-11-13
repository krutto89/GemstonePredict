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
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
                }
            df = pd.DataFrame(custom_data_input_dict)
            logger_example.info('Dataframe Gathered')
            return df
        except Exception as e:
            logger_example.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)


        