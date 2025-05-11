import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("data/processed_data.csv")
X = df[['humidity', 'wind_speed']]
y = df['temperature']

model = LinearRegression()
model.fit(X, y)

with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)
