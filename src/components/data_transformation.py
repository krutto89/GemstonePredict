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
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from src.utils.utils import save_object



# Define a class to represent a dataset
@dataclass
class DataTransformationConfig:
    pass
# @dataclass
class DataTransformation:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            logging.info("Error occured in the initiate_data_ingestion method")
            raise CustomException(e,sys)
        
