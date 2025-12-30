import csv


def read_csv(path):
    with open(path, newline='') as f:
        data = list(csv.DictReader(f))
    return data


def write_csv(path, header, rows):
    with open(path, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"')
        writer.writerow(header)
        count = 0   
        for row in rows:
            writer.writerow(row)  
            count += 1
    
    print(f"Added {count} rows to {path}")