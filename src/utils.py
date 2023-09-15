# utils will have common functionalities that the entire function going to use.

import os
import sys

import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

# function to save the pickle file  
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
# this function will apply all the models using best parameters.
def evaluate_models(X_train,y_train,X_test,y_test,models,param):
    try:
        report={}

        for i in range(len(list(models))):
            model=list(models.values())[i]
            para=param[list(models.keys())[i]]
            '''
            GridSearchCV is a technique used for hyperparameter tuning in machine learning and is part of the scikit-learn 
            library in Python. It is designed to automate the process of systematically searching for the best combination 
            of hyperparameters for a machine learning model.
            '''
            gs=GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)
            # model.fit(X_train,y_train) # Train model

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)

            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]]=test_model_score

        return report
    
    except Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return pickle.load(file_obj)
        
    except Exception as e:
        raise CustomException(e,sys)