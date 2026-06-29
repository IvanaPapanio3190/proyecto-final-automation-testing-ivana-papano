import csv
import json

def read_users_csv():
    with open("Data/users.csv",newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def read_products_json():
    with open("Data/products.json") as file:
        return json.load(file)
    