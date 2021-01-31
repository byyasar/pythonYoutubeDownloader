# -*- coding: utf-8 -*-
from pytube import YouTube



"""def progress(stream, chunk, file_handle, bytes_remaining):
    contentSize = video.filesize
    size = contentSize - bytes_remaining
    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % ('█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')

url = 'https://www.youtube.com/watch?v=yJVCztnMZfA'
yt = YouTube(url, on_progress_callback=progress)
video = yt.streams.first()
video.download()"""
def progress(chunk, file_handle, bytes_remaining):
    global filesize
    #print(filesize)
    remaining = (100 * bytes_remaining) / filesize #remaining= kalan
    step = 100 - int(remaining)
    #print("Completed:", step) # show the percentage of completed download 
    #print('\r' + '[Download progress]:[%s%s]%.2f%%;' % ('█' * int(step*20/filesize), ' '*(20-int(step*20/filesize)), float(remaining)), end='')
    print('\r' + f'Download %{step} {"█" *int((100-remaining)/2)}')


link = 'https://www.youtube.com/watch?v=VFU3JY_IjuI'
yt = YouTube(str(link), on_progress_callback=progress) # Declare YouTube
yt1 = yt.streams.get_by_itag(int(18)) # itag is given when you list all the streams of a youtube video
filesize = yt1.filesize
yt1.download()       