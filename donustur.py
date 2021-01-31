import os
import ffmpeg

###command=f'ffmpeg -i "zeynep.webm" -vn -ab 128k -ar 44100 -y "‪zeynep.mp3"';
#os.system(command)
#ffmpeg -i "zeynep.webm" -vn -ab 128k -ar 44100 -y "‪zeynep.mp3"

"""FILE1="D:\pythonyoutube\Flutter News application using GetX state management.mp4";
FILE1="D:\pythonyoutube\Flutter News application using GetX state management.mp4";
FILE2="D:\pythonyoutube\Flutter News application using GetX state management.mp3";
output_file="D:\pythonyoutube\Flutter News application using GetX state management2.mp4";

stream1=ffmpeg.input(FILE1)
stream2=ffmpeg.input(FILE2)

stream=ffmpeg.concat(stream1,stream2,v=1,a=1)"""
stream=ffmpeg.input("D:\pythonyoutube\Worst Timing Ever in Among Us! Funny Moments 82.webm")
output_file=("D:\pythonyoutube\Worst Timing Ever in Among Us! Funny Moments 82.mp3")

stream=ffmpeg.output(stream,output_file)

try:
    ffmpeg.run(stream)
except Exception as ex: 
    print(ex)

