import os
from src.reader import read_csv, write_csv
from src.layout import create_figure, Layout

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

def filter_data(data):
    region_filtered = {}
    for row in data:
        if 'pink' not in row['product']:
            continue
        
        region = row['region']
        sales = int(row['quantity']) * float(row['price'].replace('$', ''))
        date = row['date']

        if region not in region_filtered:
            region_filtered[region] = []
        region_filtered[region].append([sales, date, region]) 
    return region_filtered

def generate_output(input, output):
    os.makedirs(output_path, exist_ok=True)

    data = []
    for file in ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]:
        data.extend(read_csv(path=os.path.join(input, file)))
        
        
    # Read data and filter
    region_filtered = filter_data(data)
    output_files_path = []
    
    # Write output
    for region in region_filtered:
        filename = os.path.join(output, f'{region}_daily_sales_data.csv')
        output_files_path.append(filename)
        write_csv(filename, ['Sales', 'Date', 'Region'], region_filtered[region])
    
    return output_files_path


if __name__ == "__main__":
    ## Files
    input_path = os.path.join("data")
    output_path = os.path.join("output")
    outputs = generate_output(input_path, output_path)
    
    app = Dash()    
    df = pd.read_csv(outputs[1])
    
    figure = create_figure(df, "Date", "Sales", "Region")
    
    app.layout = Layout()\
                    .H1("SALES REPORT")\
                    .Div('Dash: A web application framework for your data.')\
                    .Figure("example-graph", figure)\
                        .Build()

    
    app.run(debug=True)
    
    