import os
import datetime
import pandas as pd


user = os.getlogin()            #имя пользователя

def date():
    date = datetime.datetime.now().strftime('%Y-%m-%d')         #получаем дату
    return date
def time():
    date_and_time = str(datetime.datetime.now()).split()            #отделяем время от даты
    time = date_and_time[1]         #берём только время
    return time

def logger(func):
    def wrapper(*args, **kwargs):
        res  = func(*args, **kwargs)
        f_name = func.__name__

        if os.path.isfile('name.csv'):
            csv = pd.read_csv('name.csv')
            columns = {'': [len(csv)], "Пользователь": [user], "Действие": [f_name],"Дата": [date()],"Время":[time()]}
            DF = pd.DataFrame(columns)
            DF.to_csv('name.csv', mode = 'a', index = False, header = False)
        else:
            columns = {"Пользователь": [user], "Действие": [f_name],"Дата": [date()],"Время":[time()]}
            DF = pd.DataFrame(columns)
            DF.to_csv('name.csv')
        return res
    return wrapper
    
@logger
def yupi():
    print("yuppi")
yupi()

