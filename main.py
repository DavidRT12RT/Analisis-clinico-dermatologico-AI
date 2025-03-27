
#Cargar y explorar los datos
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dermatology_database_1.csv");

#Muestra las primeras filas del dataset para ver su estructura
print(df.head());

#Verifica el tipo de datos de cada columna
print(df.info());

#Obtener estadísticas descriptivas de las variables numéricas
print(df.describe());

# Manejo de valores faltantes
print(df.isnull().sum()) # Cuantos valores faltantes hay en cada columna

# Analisis de la distribuccion de los atributos
#Usa histogramas (df.hist(figsize=(10,8))) para ver la distribución de las características.
df[["spongiform_pustule","family_history"]].hist(figsize=(10,8));
plt.tight_layout();
plt.title("Histogram of spongiform_pustules");
plt.show();

 