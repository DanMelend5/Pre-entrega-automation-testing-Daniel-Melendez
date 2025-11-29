import csv
#import json
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


# def leer_json_productos(ruta_archivo):
#     """
#     Lee el archivo JSON de productos
#     Retorna lista de productos para parametrización
#     """
#     ruta = pathlib.Path(ruta_archivo)
    
#     if not ruta.exists():
#         raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
    
#     with open(ruta, 'r', encoding='utf-8') as archivo:
#         productos = json.load(archivo)
    
#     return productos

# # Función para testing - ejecutar solo este archivo
# if __name__ == "__main__":
#     print("=== Probando lectura de CSV ===")
#     try:
#         casos_login = leer_csv_login('../datos/login.csv')
#         for caso in casos_login:
#             print(f"Usuario: {caso[0]}, Debe funcionar: {caso[2]}")
#     except Exception as e:
#         print(f"Error leyendo CSV: {e}")
    
#     print("\n=== Probando lectura de JSON ===")
#     try:
#         productos = leer_json_productos('../datos/productos.json')
#         for producto in productos:
#             print(f"Producto: {producto['nombre']}")
#     except Exception as e:
#         print(f"Error leyendo JSON: {e}")
