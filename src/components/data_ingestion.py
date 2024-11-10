import pandas as pd
import numpy as np
from src.logger import logger_example
from src.exception import CustomException
import logging

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import path

# Define a class to represent a dataset
@dataclass
class DataIngestionConfig:
    pass
# @dataclass
class DataIngestion:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)
        
