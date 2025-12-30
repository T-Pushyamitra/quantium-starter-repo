import os
from src.reader import read_csv, write_csv
        

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




if __name__ == "__main__":
    ## Files
    input_path = os.path.join("data", "daily_sales_data_0.csv")
    output_path = os.path.join("data", "output")
    os.makedirs(output_path, exist_ok=True)

    # Read data and filter
    data = read_csv(path=input_path)
    region_filtered = filter_data(data)
    
    
    # Write output
    for region in region_filtered:
        write_csv(os.path.join(output_path, f'{region}_daily_sales_data.csv'), ['Sales', 'Date', 'Region'], region_filtered[region])
    