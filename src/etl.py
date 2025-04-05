# Importamos Librerias
import pandas as pd

RAW_PATH = "../data/raw" # Indica el directorio donde se encuentran los datos sin transformar
PROCESSED_PATH = "../data/processed" # Indica el directorio donde se guardarán los datos transformados

# Definimos una función para extraer datos de un archivo CSV
def extract_csv_data(data):
    path = RAW_PATH + "/" + data # Concatenamos el directorio con el nombre del archivo
    return pd.read_csv(path)

# Definimos una función para extraer datos de un archivo JSON
def extract_json_data(data):
    path = RAW_PATH + "/" + data
    # Como el archivo JSON tiene múltiples líneas, usamos lines=True
    return pd.read_json(path, lines=True)

#Definimos una función para transformar el archivo json a un formato válido
def transfomr_json(data):
    # Primero, normalizamos la columna "tags", eliminando los caracteres no deseados
    data["tags"] = data["tags"].astype(str).str.replace("[", "").str.replace("]", "").str.replace("'", "").str.replace('"', "")
    # Luego, eliminamos los registros que no tienen ni descripción ni etiquetas
    data = data[(data["description"].str.strip() != "") & (data["tags"] != "")]
    return data

#Definimos una funcion para cargar los datos transformados en formato csv al directorio de salida
def load_csv_data(df, path):
    df.to_csv(path, index=False)

# Definimos una función para extraer datos de un archivo CSV
if __name__ == "__main__":
    games_md = extract_json_data("games_metadata.json")
    games = extract_csv_data("games.csv")
    recommendations = extract_csv_data("recommendations.csv")
    users = extract_csv_data("users.csv")
    games_md = transfomr_json(games_md)
    load_csv_data(games_md, PROCESSED_PATH + "/games_metadata.csv")
    load_csv_data(games, PROCESSED_PATH + "/games.csv")
    load_csv_data(recommendations, PROCESSED_PATH + "/recommendations.csv")
    load_csv_data(users, PROCESSED_PATH + "/users.csv")