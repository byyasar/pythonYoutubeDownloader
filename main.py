import colorConsole as color
import time
import app

renk = color.mycolors
downloader = app.YouTubeInstaller()


while True:
    print(f"{renk.WARNING} --------------- YouTube Mp3/Mp4 Downloader --------------- {renk.ENDC}")
    print(f"{renk.FAIL}\nÇıkış İçin => q {renk.ENDC}")
    video = input(f"{renk.OKGREEN}YouTube Link => {renk.ENDC}")
    #video = "https://www.youtube.com/watch?v=tNGfVp4KY2g&feature=push-sd&attr_tag=Q423yLv7QChYLXe8%3A6"
    if video == "q":
        print("Çıkış Yapılıyor....")
        time.sleep(0.8)
        break
    else:
        try:
            while True:
                print("\nMp4Liste=>L\nMp4 => +\nMp3 => -")
                print("Bir Üst Menü İçin => q")
                format = input("\nFormat Seçin => ")

                if format == "q":
                    break
                elif format=="l" or format=="L":
                    #mp4_liste=downloader.playListGiris(video)
                    print(f"{renk.WARNING} --------------- YouTube Mp3/Mp4 Downloader --------------- {renk.ENDC}")
                    print(f"{renk.FAIL}\nÇıkış İçin => q {renk.ENDC}")
                    print("\nMp4 => +\nMp3 => -")
                    print("Bir Üst Menü İçin => q")
                    dosya_format = input("\nFormat Seçin => ")
                    if dosya_format == "q":
                        break
                    elif dosya_format=='+':
                        app.dosya_format='mp4'
                        app.islem="-"
                    else:
                        app.dosya_format='mp3'
                    mp4_liste=downloader.playListGiris(video)
                    #print(f"{renk.OKBLUE}[TITLE] =>", mp4_liste,f"{renk.ENDC}")
                    
                elif format == "+":
                    isim = downloader.videoGiris(video)
                    print(f"{renk.OKBLUE}[TITLE] =>", isim,f"{renk.ENDC}")
                    downloader.mp4Download()
                    durum = downloader.controlDownload()
                    if durum == True:
                        break
                    else:
                        exit()
                elif format == "-":
                    isim = downloader.videoGiris(video)
                    print(f"{renk.OKBLUE}[TITLE] =>", isim,f"{renk.ENDC}")
                    downloader.mp3Download()
                    durum = downloader.controlDownload()
                    if durum == True:
                        break
                    else:
                        exit()
                else:
                    print("Geçersiz İşlem!!")
        except  Exception as e:
            print(f"{renk.FAIL}YouTube Linkini Doğru Girdiğinizden Emin Olun!{renk.ENDC} "+str(e))


print("İyi Günler...")

