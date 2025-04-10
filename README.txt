Análisis de Fiabilidad de Reseñas de Steam
===========================================

Este proyecto tiene como objetivo analizar la fiabilidad de las reseñas de usuarios en la plataforma Steam, identificando patrones y posibles indicadores de credibilidad en las evaluaciones de juegos.

Tabla de Contenidos
-------------------
- Descripción
- Instalación
- Uso
- Estructura del Proyecto
- Contribuciones
- Licencia
- Contacto

Descripción
-----------
En este proyecto, se recopilan y analizan datos de reseñas de juegos en Steam para evaluar su fiabilidad. Se utilizan técnicas de análisis de datos y visualización para identificar tendencias y patrones que puedan indicar la autenticidad y utilidad de las reseñas proporcionadas por los usuarios.

Instalación
-----------
Para ejecutar este proyecto localmente, sigue estos pasos:

1. Clona el repositorio:
   git clone https://github.com/tpadrinp/An-lisis-de-fiabilidad-de-rese-as-de-Steam.git

2. Navega al directorio del proyecto:
   cd An-lisis-de-fiabilidad-de-rese-as-de-Steam

3. Crea un entorno virtual (opcional pero recomendado):
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate

4. Instala las dependencias necesarias:
   pip install -r requirements.txt

Uso
----
Una vez instaladas las dependencias, puedes ejecutar el análisis principal con el siguiente comando:

   python main.py

Esto iniciará el proceso de análisis de las reseñas de Steam y generará los resultados correspondientes.

Estructura del Proyecto
------------------------
La estructura del proyecto es la siguiente:

Analisis-de-fiabilidad-de-resenas-de-Steam/
├── data/               # Datos utilizados para el análisis
├── notebooks/          # Jupyter Notebooks con análisis exploratorios
├── src/                # Código fuente del proyecto
│   ├── data_processing.py
│   ├── analysis.py
│   └── visualization.py
├── tests/              # Pruebas unitarias
├── main.py             # Script principal para ejecutar el análisis
├── requirements.txt    # Lista de dependencias
└── README.md           # Este archivo
