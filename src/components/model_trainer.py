import pandas as pd
import numpy as np
from src.logger import logger_example
from src.exception import CustomException

import os
import logging
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import path
from src.utils.utils import save_object, load_object
from sklearn.linear_model import LinearRegression, Ridge,Lasso,ElasticNet

# Define a class to represent a dataset
@dataclass
class ModelTrainerConfig:
    pass
# @dataclass
class ModelTrainer:
    def __init__(self):
        pass

    def initiate_model_training(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)
        
