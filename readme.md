# Proyecto de Recomendación de Juegos en Steam

## Descripción del Proyecto

Este proyecto representa una solución integral para el desarrollo de un sistema de recomendación de juegos basado en la similitud entre ellos. Aprovechando técnicas avanzadas de procesamiento de lenguaje natural y análisis de texto, la plataforma identifica juegos similares mediante la exploración de sus etiquetas y géneros. Además, se ha implementado una API que proporciona funcionalidades robustas de recomendación de juegos y análisis de datos del usuario.

## Estructura del Proyecto

- **Notebook Principal:**
  - El núcleo del proyecto está contenido en un notebook que abarca desde la Extracción, Transformación y Carga (ETL) de datos hasta el profundo Análisis Exploratorio de Datos (EDA). Asimismo, este incluye la creación de funciones esenciales para los endpoints de la API.

- **Main.py:**
  - Este archivo constituye la columna vertebral del sistema, encapsulando la lógica detrás de los endpoints que serán consumidos por la API. Aquí se encuentra la implementación de la recomendación de juegos y el análisis de datos del usuario.

- **Carpeta "Data":**
  - Almacena archivos en formato CSV y Parquet, que contienen los conjuntos de datos fundamentales utilizados en el proyecto, abarcando información sobre reviews, items y juegos de Steam.

## Preprocesamiento de Datos

Durante la fase de preprocesamiento, los datos provenientes de diversas fuentes fueron sometidos a una meticulosa transformación:

- Se realizó la desanidación de columnas con diccionarios.
- Columnas innecesarias fueron descartadas.
- Se aplicaron ajustes en formatos de fecha y tipos de datos.
- En el conjunto de reviews, se llevó a cabo un análisis de sentimiento.
- Resultando en datasets modificados, disponibles en la [carpeta "Data"](https://github.com/cristiancarandino/#).

## Recomendación de Juegos

El sistema de recomendación se fundamenta en el cálculo de similitud coseno, evaluando las afinidades entre juegos mediante sus géneros y etiquetas.

## API de Recomendación de Juegos en Steam

La API proporciona una experiencia de usuario fluida al recibir recomendaciones de juegos en la plataforma Steam. Su operatividad se desglosa en pasos claros:

1. **Entrada del Usuario:**
   - Mediante una solicitud GET a `/recomendacion_juego/{product_id}`, el usuario suministra el ID de un juego.

2. **Obtención de Datos del Juego de Referencia:**
   - La API extrae los datos del juego de referencia de un archivo CSV que contiene información detallada sobre los juegos de Steam.

3. **Procesamiento de Texto:**
   - Se fusionan las etiquetas y géneros del juego de referencia en una cadena de texto y se crea un vectorizador TF-IDF.

4. **Cálculo de Similitud:**
   - La carga de trabajo se divide en lotes, calculando la similitud coseno entre el juego de referencia y cada juego en el lote mediante el vectorizador TF-IDF.

5. **Recomendación de Juegos:**
   - Se identifican juegos similares para ofrecer recomendaciones personalizadas.

## Función "userdata"

Adicional a la función principal de recomendación, el proyecto incluye una función que, dado un ID de usuario:

- Devuelve la cantidad de dinero gastado.
- Calcula el porcentaje de juegos recomendados.
- Determina la cantidad de items en posesión del usuario.

## Links

- Repositorio (Github): [GitHub - cristiancarandino/#](https://github.com/#)
- Deploy del Proyecto (Render):[FastAPI - Swagger UI (#)](https://#)
- Video (Youtube):https://youtu.be/#

---

¡Bienvenido a la vanguardia del entretenimiento digital! Este proyecto fusiona la ciencia de datos con la diversión de los videojuegos para ofrecerte experiencias únicas. Explora, juega y descubre tus próximos favoritos con nuestro sistema de recomendación avanzado. ¡Que disfrutes al máximo tu experiencia gaming! 🎮🚀