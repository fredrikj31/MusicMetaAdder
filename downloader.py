from pytube import YouTube

def downloadVideo(url):
	yt = YouTube(url)
	print(yt.author)


def getVideoData(url):
	yt = YouTube(url)

	print(yt.thumbnail_url)

	author = yt.author.split("-")[0].strip()

	print(author)