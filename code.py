import re
import unidecode
from googleapiclient.discovery import build
import yt_dlp

# Configura tu API key de Google
YOUTUBE_API_KEY = "TU_API_KEY_DE_GOOGLE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def normalize_text(text):
    return unidecode.unidecode(text).lower()

def is_artist_in_title(title, artist):
    normalized_title = normalize_text(title)
    normalized_artist = normalize_text(artist)
    pattern = r"\b" + r"\s*".join(re.escape(char) for char in normalized_artist) + r"\b"
    return re.search(pattern, normalized_title)

def search_youtube(artist, max_results):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)
    response = youtube.search().list(
        q=artist,
        part="snippet",
        type="video",
        maxResults=max_results
    ).execute()

    videos = []
    for item in response["items"]:
        video_title = item["snippet"]["title"]
        video_id = item["id"]["videoId"]
        if is_artist_in_title(video_title, artist):
            videos.append({
                "title": video_title,
                "id": video_id,
                "link": f"https://www.youtube.com/watch?v={video_id}"
            })

    return videos

def download_video_in_mp3(video_id, output_folder="downloads"):
    ydl_opts = {
        "format": "bestaudio/best",  
        "outtmpl": f"{output_folder}/%(title)s.%(ext)s",  
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",  
                "preferredcodec": "mp3",  
                "preferredquality": "192",  
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"https://www.youtube.com/watch?v={video_id}"])

def main():
    artist = input("Ingresa el nombre del artista: ")
    if not artist:
        print("El nombre del artista es obligatorio. Intenta de nuevo.")
        return

    max_songs = input("¿Cuántas canciones deseas descargar? (Predeterminado: 5): ")
    max_songs = int(max_songs) if max_songs.strip() else 5

    mode = input("¿Modo manual o automático? (m/a, Predeterminado: a): ").strip().lower()
    mode = mode if mode in ["m", "a"] else "a"

    print(f"Buscando canciones de {artist} en YouTube...")
    results_per_search = max_songs * 3  # Aumenta el rango de búsqueda para asegurar coincidencias
    videos = search_youtube(artist, results_per_search)

    if not videos:
        print("No se encontraron videos que coincidan con el artista.")
        return

    print(f"Se encontraron {len(videos)} videos.")

    downloaded = 0
    for video in videos:
        if downloaded >= max_songs:
            break

        if mode == "m":
            print(f"Título: {video['title']}")
            print(f"Escuchar: {video['link']}")
            confirm = input("¿Descargar esta canción? (s/n): ").strip().lower()
            if confirm != "s":
                continue

        try:
            print(f"Descargando: {video['title']}...")
            download_video_in_mp3(video["id"])
            downloaded += 1
        except Exception as e:
            print(f"Error al descargar {video['title']}: {e}")

    if mode == "m" and downloaded < max_songs:
        print("Buscando canciones adicionales para completar el número solicitado...")
        remaining = max_songs - downloaded
        extra_videos = search_youtube(artist, remaining * 3)
        for video in extra_videos:
            if downloaded >= max_songs:
                break

            print(f"Título: {video['title']}")
            print(f"Escuchar: {video['link']}")
            confirm = input("¿Descargar esta canción? (s/n): ").strip().lower()
            if confirm == "s":
                try:
                    print(f"Descargando: {video['title']}...")
                    download_video_in_mp3(video["id"])
                    downloaded += 1
                except Exception as e:
                    print(f"Error al descargar {video['title']}: {e}")

    print(f"Descarga completada. Total de canciones descargadas: {downloaded}/{max_songs}")

if __name__ == "__main__":
    main()
