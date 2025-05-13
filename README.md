# Youtube Downloader

# Docker-Hub
[noris98/yt-dw](https://hub.docker.com/r/noris98/yt-dw)

# Audio Opus
YouTube suele usar webm con audio Opus (.webm + Opus audio), que:

* Funciona bien en navegadores modernos (Chrome, Firefox, Edge).
* Puede fallar en reproductores de escritorio (como Windows Media Player o reproductores sin códecs actualizados).

La solucion seria convertirl el audio a acc o mp3 o usar otro reproductor cono vlc.

# Build
```bash
docker build --tag yt-dw .
```

# Correr Imagen
```bash
docker container run --rm -v some-directory/:/app/downloads -e VIDEO_URL="https://www.youtube.com/watch?v=..." yt-dw
```