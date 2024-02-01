from fastapi import APIRouter
import pandas as pd
from fastapi.responses import JSONResponse

router = APIRouter()

# Cargar el DataFrame df_steam desde tu archivo CSV
df_steam = pd.read_csv('./Data/steam_games.csv')

@router.get("/developer/{developer}")
async def developer(developer: str):
    try:
        # Filtrar juegos por el desarrollador
        developer_games = df_steam[df_steam['developer'] == developer]

        if developer_games.empty:
            return JSONResponse(content={"message": "No se encontraron juegos para el desarrollador especificado."}, status_code=200)

        # Convertir la columna 'release_date' a tipo datetime
        developer_games['release_date'] = pd.to_datetime(developer_games['release_date'], errors='coerce')

        # Crear una nueva columna 'year' para el año de lanzamiento
        developer_games['year'] = developer_games['release_date'].dt.year

        # Filtrar juegos gratuitos
        free_games = developer_games[developer_games['price'] == 'Free to Play']

        # Contar la cantidad de items y juegos gratuitos por año
        items_by_year = developer_games.groupby('year')['id'].count().reset_index(name='Cantidad de Items')
        free_games_by_year = free_games.groupby('year')['id'].count().reset_index(name='Contenido Free')

        # Calcular el porcentaje de contenido gratuito
        items_by_year['Contenido Free'] = free_games_by_year['Contenido Free'] / items_by_year['Cantidad de Items'] * 100

        # Rellenar NaN con 0 en la columna 'Contenido Free'
        items_by_year['Contenido Free'] = items_by_year['Contenido Free'].fillna(0)

        # Ordenar por año
        items_by_year = items_by_year.sort_values('year', ascending=False)

        # Formatear el resultado
        result = items_by_year.round(2).astype({'year': int})

        return result.to_dict(orient='records')

    except Exception as e:
        return {"message": f"Error: {str(e)}"}