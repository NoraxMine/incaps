import getpass
from datetime import datetime
from datetime import date
import pandas as pd
import numpy as np



a = getpass.getuser()
print(a)
data = date.today()
time = datetime.now().time()

def true_lod(x):
    x=1

@true_lod
def f():
    print("F")

data = {'user':[a],'func_name':[f],'Ч.М.С.Мс':[time],'Д.М.Г.':[data]}

df = pd.DataFrame(data)
df = pd.concat()
print(df)

while len(df) < 100:
    a = getpass.getuser()
    print(df)
    data = date.today()
    time = datetime.now().time()
    rta = [{'column1': 'value1a', 'column2': 'value2a'}, {'column1': 'value1b', 'column2': 'value2b'}]
    data = pd.concat([df, pd.DataFrame(rta)], ignore_index=True)
else:
    print(len(df))