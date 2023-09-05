import pandas as pd
from fastapi import FastAPI

app =FastAPI()

df_games = pd.read_csv('datasets_clean/df_games.csv')
df_items = pd.read_csv('datasets_clean/df_items.csv')
df_reviews = pd.read_csv('datasets_clean/df_reviews.csv')

#http://127.0.0.1:8000

@app.get("/getUserdata/{user_id}")
def userdata(user_id:str):#Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.
    # Filtrar los items comprados por el usuario
    items_usuario = df_items[df_items['user_id'] == user_id]
    # Obtener los juegos comprados por el usuario
    juegos_comprados = df_games[df_games['id'].isin(items_usuario['item_id'])]
    #juegos_comprados = df_games.merge(items_usuario, left_on='id', right_on='item_id', how='inner')
    # Calcular la cantidad de dinero gastada
    dinero_gastado = juegos_comprados['price'].astype(float).sum()
    # Filtrar las reseñas hechas por el usuario
    reseñas_usuario = df_reviews[(df_reviews['user_id'] == user_id) & (df_reviews['recommend'] == True)]
    # Calcular el porcentaje de reseñas "True"
    porcentaje_reseñas_true = (len(reseñas_usuario) / len(df_reviews[df_reviews['user_id'] == user_id])) * 100

    return {'No de Items':len(items_usuario), 'Dinero gastado': dinero_gastado, 'Porcentaje de recomendacion': porcentaje_reseñas_true}

@app.get("/getCountreviews")
def countreviews(fecha_inicio:str, fecha_fin:str):
    # Filtrar reseñas dentro del rango de fechas
    resenias_en_rango = df_reviews[(df_reviews['posted'] >= fecha_inicio) & (df_reviews['posted'] <= fecha_fin)]
    # Contar el número total de reseñas en el rango
    total_resenias = len(resenias_en_rango)
    if total_resenias == 0:
        return 0, 0  # Si no hay reseñas en el rango, devolver 0% y 0 reseñas
    # Calcular el porcentaje de reseñas recomendadas en el rango
    porcentaje_recomendadas = (resenias_en_rango['recommend'].sum() / total_resenias) * 100
    return {"cantidad total de reseñas":total_resenias}, {"porcentaje de recomendados":porcentaje_recomendadas}

@app.get("/getGenero")
def genre(genero:str):
    # Fusionar los DataFrames en base a la columna 'item_id'
    merged_df = pd.merge(df_items, df_games, on='item_id', how='left')
    # Inicializar un diccionario para almacenar la suma de playtime_forever por género
    generos_suma = {}
    # Obtener la lista de columnas de género (variables dummies)
    columnas_genero = df_games.columns[6:]  # Asumiendo que las columnas de género comienzan desde la columna 6
    # Calcular la suma de playtime_forever por género cuando la celda de género es 1
    for columna in columnas_genero:
        generos_suma[columna] = merged_df[merged_df[columna] == 1]['playtime_forever'].sum()
    # Ordenar los géneros de forma descendente por la suma total de playtime_forever
    generos_ordenados = sorted(generos_suma.items(), key=lambda x: x[1], reverse=True)
    # Obtener la lista de géneros ordenados
    lista_generos_ordenados = [genero[0] for genero in generos_ordenados]
    posicion = (lista_generos_ordenados.index(genero))+1
    return {"Posicion en el Ranking del genero":posicion}


@app.get("/getDesarrollador")
def developer( desarrollador : str ):
    # Filtrar el DataFrame para seleccionar solo las filas del desarrollador dado
    games_filtrado = df_games[df_games['developer'] == desarrollador]
    # Convertir la columna 'release_date' al tipo de dato datetime para extraer el año
    games_filtrado['release_date'] = pd.to_datetime(games_filtrado['release_date'])
    # Extraer el año de la columna 'release_date' y contar los valores 'price' iguales a 0 por año
    anios_y_cantidad = games_filtrado.groupby(games_filtrado['release_date'].dt.year)['price'].apply(lambda x: (x == '0').sum()).reset_index()
    # Renombrar las columnas del DataFrame resultante
    anios_y_cantidad.columns = ['Anio', 'Cantidad_de_Ceros']
    # Convertir los datos a un arreglo de tuplas
    arreglo_resultante = [tuple(x) for x in anios_y_cantidad.values]
    return arreglo_resultante

@app.get("/getSentimentAnalysis")
def sentiment_analysis(anio:int):
    # Convertir la columna 'posted' al tipo de dato datetime para extraer el año
    df_reviews['posted'] = pd.to_datetime(df_reviews['posted'])
    # Filtrar las filas correspondientes al año proporcionado
    df_filtrado = df_reviews[df_reviews['posted'].dt.year == anio]
    # Contar los valores de 'sentiment_analysis' iguales a 0, 1 y 2
    conteo_0 = (df_filtrado['sentiment_analysis'] == 0).sum()
    conteo_1 = (df_filtrado['sentiment_analysis'] == 1).sum()
    conteo_2 = (df_filtrado['sentiment_analysis'] == 2).sum()
    # Crear un diccionario con los conteos
    resultados = {
        'Negative': conteo_0,
        'Neutral': conteo_1,
        'Positive': conteo_2
    }
    
    return resultados

#print(userdata('76561197970982479'))
#print(countreviews('2011-01-01','2012-01-01'))
#print(genre('Adventure'))
#print(developer('Secret Level SRL'))
print(sentiment_analysis(2013))