import pandas as pd
import numpy as no

df=pd.read_excel("order-dataset.csv")
df.head()

duplicated_count=df.duplicated().sum()
print("Number of duplicate entries: ", duplicated_count)

null_count=df.isnull().sum()
print("Number of null entries: ", null_count)

#Data Preprocessing

#Unique Market Locations of AgriFarm
df["Market"].unique()

#Convert Categorical Data of to Numerical Data to apply ML Algorithms
from sklearn.preprocessing import LabelEncoder
label_encoder=LabelEncoder()
df["Market"]=label_encoder.fit_transform(df["Market"])
df["Commodity"]=label_encoder.fit_transform(df["Commodity"])
df["Grade"]=label_encoder.fit_transform(df["Grade"])
df["Variety"]=label_encoder.fit_transform(df["Variety"])

#Dataset with Numerical Data
df.head()

#Representation of Data Graphically: HeatMap

#Selecting Features for Predicting Product Price
data_X=df.iloc[:,[4,5,6,7,9,10]].values
Y=df.iloc[:,-1].values

#Standard Scaler: Remove the mean and scales each feature/variable to unit variance
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
data_X=ss.fit_transform(data_X)

#Splitting the Data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(data_X,Y,test_size=0.2,random_state=42)

#Applying Linear Regression Model to our dataset: Makes predictions for numeric variables
#80% Data is taken for training
from sklearn.linear_model import LinearRegression 
linear_reg=LinearRegression()
linear_reg.fit(x_train,y_train)
y_predict=linear_reg.predict(x_test)

#r2 Score: (total variance explained by model) / total variance.
from sklearn.metrics import mean_squared_error, r2_score
print("r2 Score:", end= " ")
r2_score(y_test,y_predict)*100

#Applying Ridge Regression Model to our dataset
from sklearn.linear_model import Ridge
ridge_reg=Ridge(alpha=0.001)
ridge_reg.fit(x_train,y_train)
y_predict2=ridge_reg.predict(x_test)

#r2 Score: (total variance explained by model) / total variance.
from sklearn.metrics import mean_squared_error, r2_score
print("r2 Score:", end= " ")
r2_score(y_test,y_predict2)*100

#Applying Ridge Regression Model to our dataset
from sklearn.linear_model import Lasso
lasso_reg=Lasso(alpha=1.144)
lasso_reg.fit(x_train,y_train)
y_predict3=lasso_reg.predict(x_test)

#r2 Score: (total variance explained by model) / total variance.
from sklearn.metrics import mean_squared_error, r2_score
print("r2 Score:", end= " ")
r2_score(y_test,y_predict2)*100

#As the r2 score percentage of Lasso Regression is maximum, so we will use this model for deployment of our project
import pickle
filename = 'best_model.sav'
pickle.dump(lasso_reg, open(filename, 'wb'))