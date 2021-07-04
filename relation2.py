import pandas as pd
import plotly.express as px
df = pd.read_csv("iCvCDvT.csv")
graph = px.scatter(df,x="Temperature",y="Ice-cream Sales( ₹ )")
graph.show()

import csv

with open("iCvCDvT.csv",newline="")as a:
    reader = csv.reader(a)
    data = list(reader)

data.pop(0)

temperature = []
sales = []

for i in data:
    temperature.append(float(i[0]))
    sales.append(float(i[1]))

import numpy as np
relation = np.corrcoef(temperature,sales)[0,1]
print(relation)