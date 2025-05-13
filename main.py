import yt_dlp
import os
import subprocess

def download_videos(video_url):
    # Asegurarse de que la carpeta de salida exista
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join("downloads", '%(title)s.%(ext)s'),  # Ruta de salida
        'merge_output_format': 'mp4',
        'verbose': True
    }

    try:
        print(f"Descargando: {video_url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Descarga completa")
    except Exception as e:
        print(f"Hubo un problema al descargar {video_url}: {e}")

if __name__ == "__main__":
    
    try:
        subprocess.run(["ffmpeg", "-version"], check=True)

        video_url = os.getenv("VIDEO_URL")

        if video_url:
            download_videos(video_url)
        else:
            print("No se ingresaron URLs válidas.")
    except Exception as e:
        print("ffmpeg no está disponible en este contenedor:", e)

