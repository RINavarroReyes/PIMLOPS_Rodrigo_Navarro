# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

En este proyecto analisamos un dataset con videojuegos en el cual creamos distintas funciones y realizamos su correspondiete EDA y ETL

### ETL
Lo primero que hicimos fue el ETL donde tratamos el dataset para que funcionara de manera optima en las funciones

### Funciones
Desarrollamos 6 Funciones las cuales estan listadas a continuación:

- def userdata( User_id : str ): Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.

- def countreviews( YYYY-MM-DD y YYYY-MM-DD : str ): Cantidad de usuarios que realizaron reviews entre las fechas dadas y, el porcentaje de recomendación de los mismos en base a reviews.recommend.

- def genre( género : str ): Devuelve el puesto en el que se encuentra un género sobre el ranking de los mismos analizado bajo la columna PlayTimeForever.

- def userforgenre( género : str ): Top 5 de usuarios con más horas de juego en el género dado, con su URL (del user) y user_id.

- def developer( desarrollador : str ): Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora. Ejemplo de salida:

Activision	
Año	Contenido Free
2023	27%
2022	25%
xxxx	xx%
- def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.

                    Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}

### EDA
En este paso se llevo a cabo el EDA en el cual al principio cargamos el archivo que limpiamos en el paso numero 1 y en que ejecutaremos paso a paso los comandos correspondientes para poder para poder visualizar el analisis. 