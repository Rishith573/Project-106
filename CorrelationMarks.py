import plotly.express as px
import csv
import numpy as np

with open ("studentMarks.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "Days Present", y = "Marks In Percentage")


def scatterPlot():
    fig.show()
scatterPlot()

def getDataSource(data_path):
    marks = []
    days = []
    with open (data_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            marks.append(float(row["Days Present"]))
            days.append(float(row["Marks In Percentage"]))
        return{"x":marks, "y":days}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("correlation is : ", correlation[0, 1])

def setup():
    data_path = "studentMarks.csv"

    DataSource = getDataSource(data_path)
    findCorrelation(DataSource)
setup()