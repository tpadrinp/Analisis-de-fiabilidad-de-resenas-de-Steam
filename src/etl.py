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
    df_games_md = extract_json_data("games_metadata.json")
    df_games = extract_csv_data("games.csv")
    df_recommendations = extract_csv_data("recommendations.csv")
    df_users = extract_csv_data("users.csv")
    df_games_md = transfomr_json(df_games_md)
    df_games_full = df_games.merge(df_games_md, on="app_id", how="left") #Juntamos los metadatos de los juegos con la información de los juegos para obtener un dataframe de los juegos unificados
    df_reviews = df_recommendations.merge(df_users, on="user_id", how="left") #Juntamos las recomendaciones con la información de los usuarios para obtener un dataframe de las reseñas.
    load_csv_data(df_games_full, PROCESSED_PATH + "/dataset_games_full.csv")
    load_csv_data(df_reviews, PROCESSED_PATH + "/dataset_reviews.csv")