# Documentación del Proyecto

## Descripción
Este proyecto aborda la creación de un sistema de recomendación de videojuegos para usuarios en la plataforma Steam. Incluye la implementación de una API utilizando FastAPI y un análisis exploratorio de datos para comprender mejor las relaciones en el conjunto de datos.

## Estructura del Proyecto
La estructura del proyecto consta de varios módulos y carpetas, cada uno con un propósito específico:
- `main.py`: Archivo principal que inicia la aplicación FastAPI y define las rutas.
- `endpoints/`: Carpeta que contiene los módulos para diferentes endpoints de la API.
- `templates/`: Carpeta que almacena las plantillas HTML para la interfaz web.
- Otros archivos como `developer_reviews_analysis.py`, `developer.py`, y `file_info.py` que proporcionan funcionalidades específicas.

## Requisitos del Sistema
- Python 3.7 o superior
- Bibliotecas: fastapi, pandas, scikit-learn, entre otras (ver archivo `requirements.txt` para una lista completa)

## Instrucciones de Instalación
1. Clona el repositorio: `git clone https://tu-repositorio.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta la aplicación: `uvicorn main:app --reload`

## Uso de la API
### `GET /`
- Descripción: Página principal con información básica sobre la API.
- Método: GET
- Ruta: `/`

### `GET /userdata/{user_id}`
- Descripción: Devuelve información sobre el gasto, porcentaje de recomendación y cantidad de items de un usuario.
- Método: GET
- Ruta: `/userdata/{user_id}`

### `GET /recomendacion_juego/{product_id}`
- Descripción: Recomienda juegos similares a uno dado.
- Método: GET
- Ruta: `/recomendacion_juego/{product_id}`

### Otros endpoints disponibles (ver código fuente para detalles).

## Análisis Exploratorio de Datos (EDA)
- Se han realizado visualizaciones y análisis exploratorio de datos para entender mejor las relaciones y patrones en el conjunto de datos. (Ver código fuente en `etl_eda.ipynb`)

## Modelos de Aprendizaje Automático
- Se ha implementado un sistema de recomendación basado en similitud de contenido y un análisis de sentimiento en reseñas de usuarios. (Ver código fuente en `main.py` y `recomendacion_juego`)

## Despliegue
La aplicación está disponible en [Render](https://proyecto-individual-henry-ky7g.onrender.com). También hay un video explicativo en [YouTube](https://youtube.com/#).

## Recursos
- [Enlace a la aplicación](https://proyecto-individual-henry-ky7g.onrender.com)
- [Video explicativo en YouTube](https://youtube.com/#)

---
© [CRISTIAN CARANDINO] - 2024
