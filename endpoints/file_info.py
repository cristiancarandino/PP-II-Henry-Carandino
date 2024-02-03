# file_info.py

import pandas as pd
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/file-info/{file_name}")
async def get_file_info(file_name: str):
    try:
        # Definir la ruta del archivo
        file_path = f"./Data/{file_name}"

        # Leer el archivo
        if file_name.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_name.endswith('.parquet'):
            df = pd.read_parquet(file_path)
        else:
            raise HTTPException(status_code=400, detail="Formato de archivo no soportado")

        # Obtener información sobre las columnas y los primeros 5 datos
        columns_info = df.columns.tolist()
        sample_data = df.head().fillna("").to_dict(orient='records')

        return {"columns": columns_info, "sample_data": sample_data}

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
