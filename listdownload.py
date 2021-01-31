from pytube import Playlist
import app


downloader = app.YouTubeInstaller()

p = Playlist('https://www.youtube.com/watch?v=mf2BF8DFFI4&list=PLzBgi-bjxcqJ4N1yVPAO-Pdcs4PpA97do')
#print(f'Downloading: {p.title}')
for video in p.video_urls[:3]:
    print(video)
    try:
        isim = downloader.videoGiris(video)
        #downloader.mp3Download()
        islem="-"
        downloader.mp4Download(islem)
        durum = downloader.controlDownload()
    except Exception as e:
        print(e)
    