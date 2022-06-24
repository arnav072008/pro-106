import plotly.express as px
import csv

with open(r"C:\Users\shali\OneDrive\Desktop\all in one\python\C-106\icecreame.csv") as csv_file:
      df = csv.DictReader(csv_file)
      fig = px.scatter(df,x="Temperature", y="Ice-cream Sales")
      fig.show()
