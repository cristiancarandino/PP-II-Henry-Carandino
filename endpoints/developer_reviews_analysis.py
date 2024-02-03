import pandas as pd
from fastapi import APIRouter, HTTPException
import os

# Crea un objeto router para este módulo
router = APIRouter()

@router.get("/developer_reviews_analysis/{developer_name}")
async def developer_reviews_analysis(developer_name: str):
    try:
        # Cargar los datos
        steam_games_data = pd.read_csv(os.path.join('data', 'steam_games.csv'))
        reviews_data = pd.read_csv(os.path.join('data', 'reviews.csv'))

        # Filtrar reseñas por desarrollador
        reseñas_desarrollador = []
        for review in reviews_data.itertuples():
            juego = steam_games_data[steam_games_data['id'] == review.item_id]
            if not juego.empty and juego.iloc[0]['developer'] == developer_name:
                reseñas_desarrollador.append(review)

        # Contar reseñas positivas y negativas
        count_positivas = sum(1 for review in reseñas_desarrollador if review.sentiment_analysis == 2)
        count_negativas = sum(1 for review in reseñas_desarrollador if review.sentiment_analysis == 0)

        # Devolver el resultado
        resultado = {developer_name: {'Negative': count_negativas, 'Positive': count_positivas}}
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))