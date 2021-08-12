from utils.soup import MusicScraping
from utils.spotify import Spotify

def main():
    music = MusicScraping()
    spotify = Spotify()
    top_100 = music.get_top_100()
    uris = spotify.find_song_uris(top_100, music.year)
    playlist = spotify.create_playlist(f'{music.week} Billboard 100')
    spotify.add_songs_to_playlist(uris, playlist)

if __name__ == '__main__':
    main()
