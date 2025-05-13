FROM python:3.10.17-alpine3.21

# Habilitar repositorio 'community' y actualizar
RUN echo "https://dl-cdn.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories \
    && apk update \
    && apk add --no-cache ffmpeg

# cd app
WORKDIR /app

COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Crear carpeta de descargas
RUN mkdir downloads

# Destino /app porque definimos antes /app como WORKDIR
COPY main.py .

# Comando run de la imagen
CMD ["python", "main.py"]