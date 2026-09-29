#randomforestregressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

df=pd.read_csv('new_weather_data.csv')
X=df[["Time","Temperature","Feels like","Humidity","Wind","Rain"]]
y=df["arrival delay"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=62)
model = RandomForestRegressor(n_estimators=100, random_state=62)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(X_test,y_pred)
print(y_test)

# Evaluate
r2 = r2_score(y_test, y_pred)

print(f"R² Score: {r2:.3f}")



