import os
import getpass
import datetime
from datetime import date
import pandas as pd
import numpy as np

def true_lod(func):
    def wrapper(*args, **kwargs):
        user_login = os.getlogin()
        func_name = func.__name__
        current_data = date.today()
        current_time = str(datetime.now().time())


        original_resalt = func(*args, **kwargs)

        logs = "logs.csv"

        if os.path.isfile(logs):
            file_df = pd.read_csv(logs)
            data = {"": [len(file_df)], "User_login":[user_login], "Function_name":[func_name], "Data":{current_data}}
            df = pd.DataFrame(data)
            df.to_csv("logs.csv", mod = 'a', index = False, header = False)


        else:
            data = {"User_login":[user_login], "Function_name":[func_name], "Data":{current_data}}
            df = pd.DataFrame(data)
            df.to_csv("logs.csv")

        return original_resalt
    return wrapper