import sweetviz as sv
import pandas as pd

train = pd.read_csv("csv_data/train.csv")
test = pd.read_csv("csv_data/test.csv")

my_report = sv.compare([train,"Train"], [test,"Test"], "Survived")

my_report.show_html("Report.html")


