from pytube import Playlist
import app


downloader = app.YouTubeInstaller()

#p = Playlist('https://www.youtube.com/playlist?list=PLTYawZdPqADh7C8Myj5hO5KdEgLz3TtUz')
p = Playlist('https://www.youtube.com/watch?v=tLM23nkmgco&list=PLTYawZdPqADh7C8Myj5hO5KdEgLz3TtUz&index=1')
print(f'Downloading: {p.title}')
for video in p.video_urls[:2]:
    print(video)
    try:
        isim = downloader.videoGiris(video)
        #downloader.mp3Download()
        islem="+"
        app.islem=islem
        try:
            downloader.mp3Download()
            durum = downloader.controlDownload()
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)
    