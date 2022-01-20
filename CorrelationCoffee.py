import plotly.express as px
import csv
import numpy as np

with open ("coffee.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "sleep in hours", y = "Coffee in ml")
fig.show()

def scatterPlot():
    fig.show()
scatterPlot()

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open (data_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
        return{"x":coffee, "y":sleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("correlation is : ", correlation[0, 1])

def setup():
    data_path = "coffee.csv"

    DataSource = getDataSource(data_path)
    findCorrelation(DataSource)
setup()