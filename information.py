from PIL import Image
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import eyed3

from details import clientId, clientSecret

def getSongData(songName):
	sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientId,
												client_secret=clientSecret,
												redirect_uri="http://localhost:1234",
												scope="user-library-read"))

	result = sp.search(q=songName, limit=1, type="track")

	print(result)

	#* Getting artists
	for artist in result["tracks"]["items"][0]["artists"]:
		print(artist["name"])

	#* Getting image
	print(result["tracks"]["items"][0]["album"]["images"][0])
	

	#audiofile = eyed3.load("Used To Love.mp3")
	#audiofile.tag.artist = u"Python Teachers; Me"
	#audiofile.tag.save()


def setSongImage(imageURL):
	im = Image.open(requests.get(url, stream=True).raw)