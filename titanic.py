# 
import pandas as pd
# cargar información
data = pd.read_csv("titanic_data/train.csv")
test = pd.read_csv("titanic_data/test.csv")
test_ids = test["PassengerId"]
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

# operación limpieza
df_data = clean(data) 
df_test = clean(test)

# more info https://scikit-learn.org/stable/user_guide.html
# sklearn guide user manual - machine learning
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

cols = ["Sex","Embarked"]

for col in cols:
    df_data[col] = le.fit_transform(df_data[col])
    df_test[col] = le.transform(df_test[col])
    print(le.classes_)

# comprobando la limpieza de la información
print(df_data.head(10))

# Librerías para el inicio de modelo de regresión lineal
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

y = df_data["Survived"]
X = df_data.drop("Survived", axis=1)

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
clf = LogisticRegression(random_state=0, max_iter=1000).fit(X_train, y_train)

predictions = clf.predict(X_val)
from sklearn.metrics import accuracy_score
A_score = accuracy_score(y_val, predictions)
print("Accurasy score: ", A_score)

submission_preds = clf.predict(df_test)
df = pd.DataFrame({"PassengerID": test_ids.values,
                   "Survived": submission_preds, })

df.to_csv("submission.csv", index=False)

print(df)