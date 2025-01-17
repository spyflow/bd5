
# ByDownload5

**ByDownload5** is a script that allows downloading songs from YouTube in MP3 format using Google API for searching and `yt-dlp` for downloading. The user can search for songs of a specific artist and download them in two modes: **Automatic** or **Manual**.

## Features

- **Advanced Search**: Find YouTube videos of an artist, regardless of case or accents.
- Manual or Automatic Mode**: Allows you to choose how to download songs.
- Compatibility**: Download songs from YouTube in MP3 format with adjustable quality.

## Requirements

Before running the script, make sure you have the following packages installed:

- **Python 3.x**
- **Google API Client**: `pip install google-api-python-client`.
- **yt-dlp**: `pip install yt-dlp`.
- unidecode**: `pip install unidecode` **unidecode**: `pip install unidecode` **unidecode

## Configuration

### 1. Get YouTube API key
To search YouTube, you need to set up a Google API key.

1. Go to [Google Cloud Console](https://console.developers.google.com/).
2. Create a new project or select an existing one.
3. Enable the YouTube Data API.
4. Generate an **API Key** and copy it.
5. Replace `“YOUR_API_KEY_DE_GOOGLE”` in the code with your key.

### 2. Script configuration
The script file contains default settings for the API, the maximum number of songs to download and the type of download. You can modify these values in the code or through user interaction.

## Main functions

### `normalize_text(text)`.
Converts a text to lowercase and removes accents.

### `is_artist_in_title(title, artist)`.
Checks if the artist's name is present in the YouTube video title, regardless of order, capitalization or accents.

### `search_youtube(artist, max_results)`.
Performs a YouTube search on the artist's name, returning up to `max_results` results. Filters the results to include only those videos whose title contains the artist's name.

### `download_video_in_mp3(video_id, output_folder=“downloads”)`.
Download the video from YouTube in MP3 format using `yt-dlp`. The file is saved to the specified folder (by default, `downloads`).

### `main()`
Main function that handles user interaction. It allows the user to choose the artist, the number of songs to download and the download mode (automatic or manual).

## Usage Example

1. Execute the script.
2. Enter the artist name.
3. Choose the number of songs to download (default is 5).
4. Choose the download mode: **manual** or **automatic**.
5. In manual mode, the script will ask you to confirm before downloading each song.

### Example of execution:

```bash
Ingresa el nombre del artista: Queen
¿Cuántas canciones deseas descargar? (Predeterminado: 5): 
¿Modo manual o automático? (m/a, Predeterminado: a): 
Buscando canciones de Queen en YouTube...
Se encontraron 6 videos.
Título: Bohemian Rhapsody - Queen
Escuchar: https://www.youtube.com/watch?v=12345
¿Descargar esta canción? (s/n): s
Descargando: Bohemian Rhapsody - Queen...
```

### Options

- Automatic Mode**: The script will download the songs without user intervention.
- Manual Mode**: The script will display the results and ask for confirmation before downloading each song.

## Contributions

Contributing is easy! If you want to improve the script or add new features, feel free to *fork* the repository and send a *pull request*. 

1. **Clone the repository**:
    ````bash
    git clone https://github.com/spyflow/bd5.git
    ```
2. **Make your improvements** and submit your changes via a *pull request*.

## License

This project is licensed under the **MIT** license. See the [LICENSE](LICENSE) file for details.

## Author

**ByDownload5** was created by [spyflow](https://github.com/spyflow).

- GitHub: [https://github.com/spyflow/bd5](https://github.com/spyflow/bd5).

## Disclaimer

The author is not responsible for misuse or illegal use of this code. **ByDownload5** is to be used for educational and personal purposes only. It should not be used to download copyrighted content without proper authorization. Use of this script to infringe copyright or any other applicable law is the sole responsibility of the user.

---

Thank you for using **ByDownload5**! If you have any questions or suggestions, feel free to contact me.
