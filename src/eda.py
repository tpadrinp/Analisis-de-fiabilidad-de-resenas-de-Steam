# Importamos las librerias necesarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargamos los datasets
df_games_full = pd.read_csv("../data/processed/dataset_games_full.csv")
df_reviews = pd.read_csv("../data/processed/dataset_reviews.csv")
df_users = pd.read_csv("../data/processed/users.csv")

# Datos iniciales de df_games_full
print("Mostrando las primeras filas del dataset df_games_full, que contiene informacion sobre los juegos de Steam obtenida de el fichero games.csv y games_metadata.json")
df_games_full.head()

# Datos iniciales de df_reviews ordenado de más horas a menos
print("Mostrando las primeras filas del dataset df_reviews, que contiene informacion sobre las reseñas de los juegos escritas por los usuarios, obtenidos de los ficheros recommendations.csv y users.csv")
df_reviews.sort_values(by="hours", ascending=False).head

# Destribución de precio de los juegos
plt.figure(figsize=(10, 5))
sns.histplot(df_games_full["price_original"], bins=110, kde=True)
plt.title("Distribución del Precio Original de los Juegos")
plt.xlabel("Precio Original")
plt.xlim(0, 110)
plt.xticks(np.arange(0, 110, 10))
plt.show()

# Distribución de etiquetas más usadas en los juegos
df_games_full["tags"].str.split(", ").explode().value_counts().head(15).plot(kind="barh", title="Top 15 Tags Más Comunes")
plt.gca().invert_yaxis()
plt.show()

# Descripcion de los datos products y reviews de df_users
df_users[["products", "reviews"]].describe()

# Distribución pictográfica de Precio Orignal vs Valoración
plt.figure(figsize=(10, 5))
sns.regplot(data=df_games_full, x="price_original", y="positive_ratio", scatter_kws={'alpha':0.5}, line_kws={"color": "red"})
plt.title("Regresión entre Precio Original y Valoración Positiva")
plt.xlabel("Precio Original")
plt.ylabel("Valoración Positiva")
plt.show()

# Distribución de Precio Original y Valoración Positiva. Se utiliza la función kde=True para mostrar la densidad de probabilidad estimada
plt.figure(figsize=(10, 5))
sns.histplot(df_games_full["price_original"], kde=True, color='blue', label="Precio Original", stat="density", bins=30)
sns.histplot(df_games_full["positive_ratio"], kde=True, color='green', label="Valoración Positiva", stat="density", bins=30)
plt.title("Distribución de Precio Original y Valoración Positiva")
plt.legend()
plt.xlim(0, 100)
plt.xticks(np.arange(0, 110, 10))
plt.show()

