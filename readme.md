# Proyecto de Recomendación de Juegos - Steam

![Portada del Proyecto](./templates/portada.jpg)

Este proyecto se centra en el desarrollo de un sistema de recomendación de videojuegos para usuarios de la plataforma Steam, abordando aspectos desde el tratamiento de datos hasta la implementación de una API RESTful.

## Objetivos

- Implementar un sistema de recomendación de videojuegos.
- Crear una API para acceder y consultar datos relacionados con la plataforma Steam.

## Estructura del Proyecto

El proyecto consta de varios módulos y endpoints de API:

- **main.py**: Contiene el código principal de la API FastAPI.
- **endpoints/developer_reviews_analysis.py**: Módulo para el análisis de reseñas por desarrollador.
- **endpoints/file_info.py**: Módulo para obtener información sobre archivos.
- **endpoints/developer.py**: Módulo para estadísticas de desarrolladores.
- Otros módulos para recomendación de juegos, análisis de usuario, y más.

## Configuración y Ejecución

1. Instalar las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

2. Ejecutar la aplicación:

    ```bash
    uvicorn main:app --reload
    ```

La aplicación estará disponible en [https://proyecto-individual-henry-ky7g.onrender.com](https://proyecto-individual-henry-ky7g.onrender.com).

## Endpoints de la API

- **GET /userdata/{user_id}**: Devuelve información sobre el gasto, porcentaje de recomendación y cantidad de items de un usuario.
- **GET /recomendacion_juego/{product_id}**: Recomienda juegos similares a un juego dado.
- **GET /developer/{developer}**: Proporciona estadísticas sobre juegos de un desarrollador.
- **GET /file-info/{file_name}**: Obtiene información sobre archivos.
- Otros endpoints según las especificaciones del proyecto.

## Análisis Exploratorio de Datos (EDA)

La sección de EDA se encuentra en el código principal y genera gráficos para explorar relaciones y patrones en los datos.

## Modelo de Aprendizaje Automático

El código incluye la implementación de un sistema de recomendación basado en la similitud del coseno.

## Recursos

- La aplicación está disponible en: [https://proyecto-individual-henry-ky7g.onrender.com](https://proyecto-individual-henry-ky7g.onrender.com)
- Video explicativo del funcionamiento de la aplicación: [YouTube](https://youtu.be/x6OcjSShNQI)
