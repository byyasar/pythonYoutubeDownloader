"""from pytube import YouTube
#YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()
yt = YouTube('https://www.youtube.com/watch?v=teyr-2tl1Wo')
liste=yt.streams.filter(progressive=True,file_extension='mp4',).order_by('resolution').desc()
print(liste)
... 
... .order_by('resolution')
... .desc()
... .first()
... .download()"""

#pip install MoviePy

#import moviepy.editor as moviepy
#clip = moviepy.VideoFileClip("Flutter Temiz İyi Uyumlu(Responsive) Kod Düşüncesi ve Geliştirme.mp4")
#aduio=moviepy.AudioFileClip("Zeynep Bastık - Uslanmıyor Bu.webm")
#clip=clip.set_audio(aduio)
#clip.write_videofile("Flutter Temiz İyi Uyumlu(Responsive) Kod Düşüncesi ve Geliştirme2.mp4",fps=60)
#moviepy.AudioClip.file

#
import os
print(f'yol:{os.getcwd()}')
