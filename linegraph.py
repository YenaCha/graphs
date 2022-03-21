import pandas as pd
import plotly.express as px
df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 103/csv files/line_chart.csv')
graph = px.line(df,x = 'Year', y = 'Per capita income', color = 'Country')
graph.show()