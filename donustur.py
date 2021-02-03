import ffmpeg
import colorConsole as color
import os

###command=f'ffmpeg -i "zeynep.webm" -vn -ab 128k -ar 44100 -y "‪zeynep.mp3"';
#os.system(command)
#ffmpeg -i "zeynep.webm" -vn -ab 128k -ar 44100 -y "‪zeynep.mp3"
renk = color.mycolors

print(f"{renk.FAIL}\nÇıkış İçin => q {renk.ENDC}")
FILE1 = os.getcwd() +'/'+ input(f"{renk.OKGREEN}Video linki gir => {renk.ENDC}")+'.mp4'
FILE2 = os.getcwd()+'/'+ input(f"{renk.OKGREEN}Ses linki gir => {renk.ENDC}")+'.webm'
output_file = os.getcwd()+'/1080p.mp4'
#print(f'\n{FILE1}\n{FILE2}\n{output_file}')
"""FILE1="D:\pythonYoutubeDownlaoder\mp4\PDF in Flutter Creation and Preview.mp4";
FILE2="D:\pythonYoutubeDownlaoder\mp4\PDF in Flutter Creation and Preview.webm";
output_file="D:\pythonYoutubeDownlaoder\mp4\PDF in Flutter Creation and Preview1080.mp4";"""

stream1=ffmpeg.input(FILE1)
stream2=ffmpeg.input(FILE2)

stream=ffmpeg.concat(stream1,stream2,v=1,a=1)
stream=ffmpeg.output(stream,output_file)

try:
    ffmpeg.run(stream)
except Exception as ex: 
    print(ex)

