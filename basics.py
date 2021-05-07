import numpy
import pandas as pd
import sklearn 
import matplotlib

df = pd.read_csv('train.csv')

"""
### VIEWING LOADING , using panda 

print(df)
print(df.size)
print(df.describe())   #print details

print(df.info())
print(df.sample())
print(df.columns)
"""

pd.set_option('display.max_column',None)
pd.set_option('display.max_rows',None)
#df['Ticket'] = 0
#del df['Ticket']
print(df['Ticket'])

