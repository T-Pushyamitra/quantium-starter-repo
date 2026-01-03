import os
from pathlib import Path

from src.data_reader import filter_sales_data, read_input, create_chart, write_to_csv
from dash import Dash, html, dcc, callback, Input, Output
import pandas as pd

app = Dash(__name__)



@callback(
    Output("sales-chart", "figure"),
    Input("region", "value"))
def read_filters(value):
    return create_chart(region_filtered, value)


## Files
BASE_DEFAULT_PATH = Path(__file__).resolve().parent

source = os.path.join(BASE_DEFAULT_PATH, "data")
output = os.path.join(BASE_DEFAULT_PATH, "output")
os.makedirs(output, exist_ok=True)        

sales_data_frame = read_input(source)

## Filter the data
region_filtered = filter_sales_data(sales_data_frame, "pink morsel")

for region, rdf in region_filtered.groupby("Region"):
    write_to_csv(rdf, os.path.join(output, f"{region}_daily_sales_data.csv"))

## Get all the unique regions
    
regions = region_filtered["Region"].dropna().unique().tolist()
regions_option = [{'label' : i.upper(), 'value': i} for i in regions]
regions_option.append({'label' : 'ALL', 'value': 'ALL'})

## Create first chart
figure = create_chart(region_filtered, "ALL")
    
    
app.layout = html.Div(
    [
        html.H1("Sales Analysis", id="heading"),

        html.P(
            "Select a time range to update the chart below.", id="description"
        ),
        html.Div([
            dcc.RadioItems(id='region', options=regions_option,  value='ALL', inline=True)
        ]),
        html.Div(children=[dcc.Graph(id="sales-chart", figure=figure)])
    ],
    style={
        "display": "flex",
        "flexDirection": "column",
        "gap": "20px",
        "maxWidth": "900px",
        "margin": "auto",
        "padding": "20px",
    })
    

if __name__ == "__main__":
    app.run(debug=True)
    
    