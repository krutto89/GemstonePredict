import os 
import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.logger import logger_example
from src.exception import CustomException

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_squared_log_error

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
    return f"Object saved successfully at {file_path}"


def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(X_train, y_train)

            # Make predictions
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Calculate metrics
            mae = mean_absolute_error(y_test, y_test_pred)
            mse = mean_squared_error(y_test, y_test_pred)
            rmse = np.sqrt(mse)
            r2_square = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = {
                'mae': mae,
                'mse': mse,
                'rmse': rmse,
                'r2_square': r2_square

            }
            logger_example.info(f"Model {list(models.keys())[i]} trained and evaluated successfully.")
            save_object(f"models/model_{list(models.keys())[i]}.pkl", model)
        return report
    except Exception as e:
        logger_example.error(f"Error occurred while evaluating models: {str(e)}")
        return None
    finally:
        logger_example.info("Evaluation completed.")


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            obj = pickle.load(file_obj)
        return obj
    except Exception as e:
        logger_example.error(f"Error occurred while loading object: {str(e)}")
        return None
    