import pandas as pd
import plotly.graph_objects as go
import csv

import plotly.express as px
df = pd.read_csv("data.csv")
Mean = df.groupby(["student_id","level"], as_index = False)["attempt"].mean()
fig = px.scatter(Mean , x="student_id" , y="level",size = "attempt", color = "attempt")
fig.show()