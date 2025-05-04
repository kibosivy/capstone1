# Import libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="df7044f104d94b9eb9b9b42424fe65ba",
    client_secret="448c3ff296204cdfaf04174527ca0c7c",
    redirect_uri="http://127.0.0.1:8888/callback", 
    scope="playlist-modify-public user-top-read"
))

# Search for tracks
search_term = input("Search for a track or artist: ")
results = sp.search(search_term, limit=20, type='track')
tracks = results['tracks']['items']

# Show track results
print("\n Search Results:")
for i, track in enumerate(tracks):
    print(f"{i}: {track['name']} by {track['artists'][0]['name']}")

# Select multiple track numbers
choices = input("\n Choose track numbers to add (comma-separated, e.g. 0,2,4): ")

# Get URIs and names of selected tracks
chosen_indices = [int(i.strip()) for i in choices.split(',')]
track_uris = [tracks[i]['uri'] for i in chosen_indices]
track_names = [tracks[i]['name'] for i in chosen_indices]

# Get current user and create a new playlist
user_id = sp.current_user()['id']
playlist_name = input("\n Enter a name for your new playlist: ")
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
playlist_id = playlist['id']

# Add selected tracks to the playlist
sp.playlist_add_items(playlist_id, track_uris)
print(f"\n Added the following tracks to your playlist '{playlist_name}':")
for name in track_names:
    print(f" {name}")
