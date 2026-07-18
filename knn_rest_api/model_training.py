import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import pickle

# Importing data
df=pd.read_csv("C:\\Users\\HARSHITA\\OneDrive\\Data_sets\\covid_toy - covid_toy.csv")
df.head()

x=df.drop(columns=['has_covid'])
y=df['has_covid']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

numerical_feature = x.select_dtypes(exclude=['object', 'string']).columns

categorical_feature = x.select_dtypes(include=['object', 'string']).columns


numeric_pipeline=Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='mean')),
    ('scalling',StandardScaler())
])

categorical_pipeline=Pipeline(steps=[
    ('impute',SimpleImputer(strategy='most_frequent')),
    ('onehot',OneHotEncoder(sparse_output=False, handle_unknown='ignore'))
])

preprocessor=ColumnTransformer(transformers=[
    ('num',numeric_pipeline,numerical_feature),
    ('cat',categorical_pipeline,categorical_feature)
])

knn=Pipeline(steps=[
    ('preprocessor',preprocessor),
    ('sample',SMOTE(random_state=42)),
    ('classfier',KNeighborsClassifier(n_neighbors=3))
])

knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)
pickle.dump(knn,open("knn.pkl","wb"))