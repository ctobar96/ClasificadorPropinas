# Reestructuracion y evaluacion
==============================

Proyecto realizado para el curso de Desarrollo de proyectos y productos de datos, impartido por el profesor Alonso Astroza. El trabajo consiste en la reestructuración y evaluación de un modelo de Machine Learning entregado por el docente.



-----
## Instalación

1. Clona el respositorio 

```bash
git clone https://github.com/ctobar96/ClasificadorPropinas.git

cd proyecto-clasificacion
```

2. Crea y activa un entorno virtual
```bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
```

3. Instalación de dependencias
```bash
pip install -r requirements.txt
```

## Ejecución
Para ejecutar el proyecto 
```bash
00_nyc_taxi_model.pynb
```
------


# Organización del proyecto
------------

    ├── LICENSE            <- Contiene la licencia del proyecto, especificando los términos legales 
                            bajo los cuales se puede usar, modificar o distribuir el código.
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- Descripción del proyecto y cómo ejecutarlo.
    ├── data
    │   ├── external       <- Datos obtenidos de fuentes externas.
    │   ├── interim        <- Datos intermedios que han sido transformados parcialmente.
    │   ├── processed      <- Datos transformados para entrenamiento/pruebas.
    │   └── raw            <- Datos originales descargados.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details****
    │
    ├── models             <- Guarda los modelos entrenados, predicciones generadas y resúmenes 
                            relacionados con los modelos.
    │
    ├── notebooks          <- Contiene cuadernos Jupyter (.ipynb) utilizados para explorar datos, 
                            realizar análisis iniciales o documentar experimentos
    │
    ├── references         <- Almacena materiales explicativos como diccionarios de datos, manuales, 
                            documentación externa y cualquier otro recurso que ayude a entender los datos o el proyecto.
    │
    ├── reports            <- Contiene resultados generados del análisis, como informes en formato 
                            HTML, PDF, LaTeX, etc.
    │   └── figures        <- Guarda gráficos y figuras generadas durante el análisis para 
                            incluirlas en los informes.
    │
    ├── requirements.txt   <- Archivo que lista las dependencias necesarias para reproducir el 
                            entorno del proyecto. Se genera típicamente con el comando pip freeze > requirements.txt. 
                            Permite a otros instalar las mismas versiones de librerías utilizadas en el análisis.
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Contiene el código fuente del proyecto organizado por funcionalidad:
    │   ├── __init__.py    <- La carpeta src es unmódulo de python.
    │   │
    │   ├── data           <- Script para descargar, limpiar o preparar datasets.
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <-  Script para crear nuevas variables o transformar las existentes.
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts relacionados con el entrenamiento y uso de modelos predictivos.
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts para crear visualizaciones exploratorias o resultados finales. 
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
