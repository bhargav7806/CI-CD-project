import os 
import sys 
import dill


import numpy as np 
import pandas as pd 
from src.exception import CustomException




def save_object(file_path , obj):
    try:
        dir_path = os.path.dirname(file_path) ## dirname give all foler except last file name 

        os.makedirs(dir_path , exist_ok = True)

        with open(file_path , 'wb') as file_obj:
            dill.dump(obj , file_obj)   ## file saved in specific file path


    except Exception as e:
        raise CustomException(e , sys)