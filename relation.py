import pandas as pd
import plotly.express as px
df = pd.read_csv("Student Marks vs Days Present.csv")
graph = px.scatter(df,x="Marks In Percentage",y="Days Present")
graph.show()

import csv

with open("Student Marks vs Days Present.csv",newline="")as a:
    reader = csv.reader(a)
    data = list(reader)

data.pop(0)

marks = []
present = []

for i in data:
    marks.append(float(i[1]))
    present.append(float(i[2]))

import numpy as np
relation = np.corrcoef(marks,present)[0,1]
print(relation)

# 1 : highly correlated
# 0 : no related
# -1 : inversely related