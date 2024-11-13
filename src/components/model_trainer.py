import pandas as pd
import numpy as np
from src.logger.logger_example import logger_example
from src.exception.exception import CustomException
import os
import sys
import logging
from dataclasses import dataclass
from pathlib import Path

from src.utils.utils import save_object, evaluate_models
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_training(self, train_array, test_array):
        try:
            logger_example.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet()
            }
            
            model_report = evaluate_models(X_train, y_train, X_test, y_test, models)
            print(model_report)
            print('\n====================================================================================\n')
            logger_example.info(f'Model Report : {model_report}')

            # To get the best model based on r2_square
            best_model_name, best_model_metrics = max(
                model_report.items(),
                key=lambda item: item[1]['r2_square']
            )
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_metrics["r2_square"]}')
            print('\n====================================================================================\n')
            logger_example.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_metrics["r2_square"]}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
          
        except Exception as e:
            logger_example.error('Exception occurred at Model Training')
            raise CustomException(e, sys)
