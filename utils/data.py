import csv
import json
import pathlib

def read_csv_login(file_route):
    """
    Lee el archivo CSV de credenciales de login
    Retorna lista de tuplas para pytest.mark.parametrize
    """
    data = []
    route = pathlib.Path(file_route)
    
    if not route.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {route}")
    
    with open(route, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            valid_credentials = row['valid_credentials'].lower() == 'true'
            data.append((
                row['username'], 
                row['password'], 
                valid_credentials,
                row['description']
            ))
    
    return data


def read_json_products(file_route):
    route = pathlib.Path(file_route)
    
    if not route.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {route}")
    
    with open(route, 'r', encoding='utf-8') as file:
        products = json.load(file)
    
    return products
