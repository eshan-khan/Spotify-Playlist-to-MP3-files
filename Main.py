import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp
import os 

os.system("pip install -r requirements.txt")


def spotify_playlist(link):
    client_id = '4bcbba261e9641129fd3bfd08a6e72eb'
    client_secret = '    '

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlist_link = link
    playlist_id = playlist_link[(playlist_link.rfind("/")+1):]

    songs = []
    limit = 100
    offset = 0

    while True:
        results = sp.playlist_items(playlist_id, limit=limit, offset=offset)
        items = results['items']

        if not items:
            break

        for item in items:
            track = item['track']
            if track:  
                songs.append((track['name'],track['artists'][0]['name']))

        offset += limit


    return songs

def Playlist_Downloader(Songs):
    for index,song in enumerate(Songs):
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,  
            'outtmpl': 'Downloads/%(title)s.%(ext)s',  
            'quiet':True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',  
            }]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{song[0]} {song[1]} lyrics"])

link=input("Paste the link of the playlist (MUST BE A PUBLIC PLAYLIST):\n")
Songs=spotify_playlist(link);    
Playlist_Downloader(Songs);

