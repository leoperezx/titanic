# 
import pandas as pd

data = pd.read_csv("titanic_data/train.csv")
test = pd.read_csv("titanic_data/test.csv")

print(data.head(5))

def clean(data):
    # .drop(["col1","col2",...]) retiras las columnas del dataframe
    data = data.drop(["PassengerId","name","Ticket","Cabin"]) 