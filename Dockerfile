# Usar una imagen de Airflow con Python 3.8
FROM apache/airflow:2.5.1-python3.8

# Cambiar al usuario root para instalar dependencias del sistema
USER root

# Instalar git (u otras dependencias del sistema si es necesario)
RUN apt-get update && apt-get install -y git

# Cambiar al usuario airflow
USER airflow

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt