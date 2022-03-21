import pandas as pd
import plotly.express as px
df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 103/csv files/data.csv')
graph = px.bar(df,x = 'Country',y = 'Population')
graph.show()