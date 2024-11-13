import pandas as pd
import numpy as np
from src.logger import logger_example
from src.exception.exception import CustomException
import logging

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

# Define a class to represent a dataset
@dataclass
class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifact","raw.csv")
    train_data_path:str=os.path.join("artifact","train.csv")
    test_data_path:str=os.path.join("artifact","test.csv")
# @dataclass
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")
        try:
            data = pd.read_csv(r'C:\Users\rutto\OneDrive\Desktop\ml-End2End\GemstonePredict\data.csv')
            logging.info("Dataset read successfully")
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Dataset saved successfully in the artefact folder")

            train_set,test_set=train_test_split(data,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False)

            logging.info("Training dataset saved successfully in the artefact folder")
            test_set.to_csv(self.ingestion_config.test_data_path,index=False)
            logging.info("Testing dataset saved successfully in the artefact folder")

            logging.info("Data Ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )



        except Exception as e:
            logging.info()
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()