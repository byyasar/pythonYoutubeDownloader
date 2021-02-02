from pytube import YouTube
import colorConsole as color
import os
import random
#from pytube.cli import on_progress
import ffmpeg

renk = color.mycolors
filesize=0
islem=""


class YouTubeInstaller:

    def __init__(self,ytLink = "",iTag=0,downloadDurum= False, videoAdi = "", resolitions = [["360p","+",18],["720p","-",22],["1080p","*",299]]):
        self.ytLink = ytLink
        self.videoAdi = videoAdi
        self.resolitions = resolitions
        self.iTag = iTag
        self.downloadDurum = downloadDurum

        

    def videoGiris(self,video):
        print("İşleniyor...")
        self.ytLink = YouTube(video,on_progress_callback=self.progress)
        self.videoAdi = self.ytLink.title
        return self.videoAdi

    def bul(self,cevap):
        for i in range(len(self.resolitions)):
            if cevap == self.resolitions[i][1]:
                return self.resolitions[i][2]


    def mp4Download(self):
        global islem
        liste = list(self.ytLink.streams.filter(progressive=True,file_extension="mp4"))
        #liste = self.ytLink.streams.filter(file_extension="mp4").order_by('resolution')
        hdliste=list(self.ytLink.streams.filter(file_extension='mp4').order_by('resolution').desc())
        #liste.extend(hdliste)
        #print(type(list(liste))) 
       #print(type(list(hdliste)))
        liste.extend(hdliste)
        print(liste)
        print("\n\n")
        print(f'Gelen islem={islem}')
        for i in range(3):
            print(self.resolitions[i][0], " => ", self.resolitions[i][1])
        if(islem==""):
            islem = input("\n\nÇözünürlük Seçin =>")
            print(f'seçilen islem={islem}')
        #iTag Seçildi
            self.iTag = self.bul(islem)
            self.ytDownload('mp4')
        islem==""
 
    def controlDownload(self):
        return self.downloadDurum

    def progress(self,chunk, file_handle, bytes_remaining):
        global filesize
        #print(filesize)
        remaining = (100 * bytes_remaining) / filesize #remaining= kalan
        step = 100 - int(remaining)
        #print("Completed:", step) # show the percentage of completed download 
        #print('\r' + '[Download progress]:[%s%s]%.2f%%;' % ('█' * int(step*20/filesize), ' '*(20-int(step*20/filesize)), float(remaining)), end='')
        print (f'\rDownload %{step} {"█" *int((100-remaining)/2)}',end="")

    def ytDownload(self,dosya_format):
        try:
            global filesize
            konum = os.getcwd()
            stream = self.ytLink.streams.get_by_itag(self.iTag)
            print(stream)
            print(f'Dosya boyutu: {stream.filesize}')
            filesize=stream.filesize
            print(f"{renk.OKGREEN}İndirme İşlemi Başladı! Lütfen Bekleyin... {renk.ENDC}")
            if dosya_format=='mp4':
                stream.download(konum+"/mp4/")
            else:
                stream.download()
            
            print(f"{renk.OKBLUE}İndirme İşlemi Tamamlandı! {renk.ENDC}")
            print("Dosya Konumu : {0}\{1}".format(konum,self.videoAdi))
            self.downloadDurum = True
        except Exception as error:
            self.downloadDurum = False
            print("Hata : ",str(error))
            #output_file=path+"/mp3/"+file_name+".mp3"

    def uznatiDegistir(self,dosyaAdi,yeniIsım,yeniUzanti):
        try:
            yeniIsım,ext = os.path.splitext(dosyaAdi)
            os.rename(dosyaAdi,yeniIsım+yeniUzanti)
        except FileExistsError:
            rndSayi = random.randint(0,99)
            yeniIsım,ext = os.path.splitext(dosyaAdi)
            os.rename(dosyaAdi,yeniIsım+str(rndSayi)+yeniUzanti)

    def titleArindir(self,zTitle):
        zTitle = zTitle.replace("/","")
        zTitle = zTitle.replace(".","")
        #zTitle = zTitle.replace("#","")
        return zTitle

    def mp3Download(self):
        liste = self.ytLink.streams.filter(only_audio=True)
        self.iTag = 251
        self.ytDownload('mp3') 

        #yeniDosyaAdi = self.titleArindir(self.videoAdi)
        #self.uznatiDegistir(self.videoAdi,yeniDosyaAdi,".webm")
        try:
            print("Mp3 dönüştürülüyor")
            self.mp3Donustur(self.videoAdi)
        except Exception as ex:
            print(f'Dönüştürme hatası oluştu {ex}')
    
    def mp3Donustur(self,file_name):
        path=os.getcwd()
        output_file=path+"/mp3/"+file_name+".mp3"
        input_file= path+"/"+file_name+".webm"
        input_file = input_file.replace("#","")
        stream=ffmpeg.input(input_file)
        stream=ffmpeg.output(stream,output_file)
        try:
            ffmpeg.run(stream)
        except Exception as ex: 
            print(f'Dönüştürme hatası oluştu {ex}')
        durum = self.downloadDurum
        if durum == True:
            try:
                print(f'silinecek dosya {input_file}')
                os.remove(input_file)
            except Exception as ex: 
                print(f'Silme hatası oluştu {ex}')


















###
