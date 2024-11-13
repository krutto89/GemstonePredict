import pandas as pd
import numpy as np
from src.logger.logger_example import logger_example
from src.exception.exception import CustomException
from sklearn.metrics import accuracy_score,mean_squared_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import pickle
import logging


import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from src.utils.utils import save_object,load_object



# Define a class to represent a dataset
@dataclass
class ModelTransformationConfig:
    pass
# @dataclass
class ModelEvaluation:
    def __init__(self):
        pass

    def initiate_model_evaluation(self,train_array,test_array):
        try:
            pass
        except Exception as e:
          logging.info()
          raise CustomException(e,sys)
        
