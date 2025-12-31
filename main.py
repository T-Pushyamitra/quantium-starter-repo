import os

from src.data_reader import filter_sales_data, read_input
from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px

@callback(
    Output("sales-chart", "figure"),
    Input("region", "value"))
def read_filters(value):
    print(value)
    if value == "ALL":
        return px.line(region_filtered, "Date", "Sales", "Region") 
    return px.line(region_filtered[region_filtered['Region'] == value], "Date", "Sales", "Region")
    

if __name__ == "__main__":
    ## Files
    source = os.path.join("data")
    output = os.path.join("output")
    os.makedirs(output, exist_ok=True)        
    
    sales_data_frame = read_input(source)
    
    ## Filter the data
    region_filtered = filter_sales_data(sales_data_frame, "pink morsel")
    
    for region, r in region_filtered.groupby("Region"):
        r.to_csv(os.path.join(output, f"{region}_daily_sales_data.csv"), index=False)

    regions = region_filtered["Region"].dropna().unique().tolist()
    
    regions_option = { i: i.upper() for i in regions}
    regions_option["ALL"] = "ALL"
    
    app = Dash()
        
    figure = px.line(region_filtered, "Date", "Sales", "Region")
    
    app.layout = html.Div(
    [
        html.H1("Sales Analysis"),

        html.P(
            "Select a time range to update the chart below."
        ),

        dcc.RadioItems(
            id="region",
            options=regions_option,
            value='ALL',
            inline=True,
        ),

        dcc.Graph(id="sales-chart", figure=figure),
    ],
    style={
        "display": "flex",
        "flexDirection": "column",
        "gap": "20px",
        "maxWidth": "900px",
        "margin": "auto",
        "padding": "20px",
    })
    
    app.run(debug=True)
    
    