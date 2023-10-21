# Imagen base
FROM python:3.10.13-slim-bullseye
# Establecer variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Establecer directorio de trabajo
WORKDIR /app
# Instalar dependencias
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# Copiar el proyecto
COPY . .
