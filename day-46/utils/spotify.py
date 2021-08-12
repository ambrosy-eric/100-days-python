import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

class Spotify():
    """
    Class for interfacing with Spotify API
    """
    def __init__(self):
        self.client = os.environ.get('SPOTIFY_ID')
        self.secret = os.environ.get('SPOTIFY_SECRET')
        self.client = self.configure_client()
        self.user = self.client.current_user()['id']

    def configure_client(self):
        """
        Configure Spotify client
        """
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=self.client,
                client_secret=self.secret,
                redirect_uri="http://example.com",
                scope="playlist-modify-private"
            )
        )

        return sp

    def find_song_uris(self, songs, year):
        """
        Given a list of songs and artists
        Find them and return their list of URIs
        """
        uris = []
        for song in songs:
            result = self.client.search(q=f'track:{song} year:{year}', type='track')
            try:
                uri = result['tracks']['items'][0]['uri']
                uris.append(uri)
            except IndexError:
                print(f'{song} could not be found. Skipped')
        return uris

    def create_playlist(self, playlist_name='AutoPlaylist'):
        """
        Given a playlist name
        Create a new playlist
        """
        playlist = self.client.user_playlist_create(user=self.user, name=playlist_name, public=False)
        return playlist

    def add_songs_to_playlist(self, song_uris, playlist):
        """
        Given a list of song URIs
        Add those songs to a specified playlist"""
        self.client.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
