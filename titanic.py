# 
import pandas as pd
# cargar información
data = pd.read_csv("titanic_data/train.csv")
test = pd.read_csv("titanic_data/test.csv")
# comprobando la carga de información
print(data.head(5))

def clean(data):
    '''
    Función que realiza operaciones de limpieza con la información que
    incluye retirar algunas columnas y rellenar con el valor estadistico 
    de la media, todo los valores en blanco de las columnas que se 
    conservan.
    '''
    # .drop(["col1","col2",...]) retiras las columnas del dataframe
    data = data.drop(["PassengerId","Name","Ticket","Cabin"], axis=1) 

    cols =["Age","SibSp","Parch","Fare"] # columnas con espacios en blanco
    for col in cols:
        data[col].fillna(data[col].median(), inplace=True)
        # Rellenado los espacios en blanco con el valor de la media de toda la columna
    
    # Rellena los espacios en blanco de la columna Embarked con la letra "U"
    data.Embarked.fillna("U", inplace=True)
    return data

df_data = clean(data)
df_test = clean(test)

print(df_data.head(10))



# more info https://scikit-learn.org/stable/user_guide.html
# sklearn guide user manual - machine learning
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

cols = ["Sex","Embarked"]

for col in cols:
    df_data[col] = le.fit_transform(df_data[col])
    df_test[col] = le.transform(df_test[col])
    print(le.classes_)

print(df_data.head(10))