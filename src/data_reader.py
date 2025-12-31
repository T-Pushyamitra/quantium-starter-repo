import os
import pandas as pd

def filter_sales_data(data, product, region=None, price__le=0, price__ge=0):
    
    filtered_data = data[data["Product"] == product]
    
    if region:
        filtered_data = data[data["Region"] == region]
    
    if price__le and price__ge:
        filtered_data = data[data["Sales"] <= price__le & data["Sales"] >= price__ge]
    elif price__le:
        filtered_data = data[data["Sales"] <= price__le]
    elif price__ge:
        filtered_data = data[data["Sales"] >= price__ge]
        
    return filtered_data

def read_input(source):
    df = pd.concat([pd.read_csv(os.path.join(source, f)) for f in os.listdir(source)], ignore_index=True)
    df["price"] = df["price"].str.replace("$", "").astype(float)
    df["sales"] = df["quantity"] * df["price"]
    df = df[["sales", "product", "date", "region"]]
    df = df.rename(columns={
    "sales": "Sales",
    "date": "Date",
    "product": "Product",
    "region": "Region"
    })
    df = df.sort_values("Date")
    return df
      