# pythonYouTubeDownloader
# Kurulumlar


python -m pip uninstall pytube pytube3 pytubex
python -m pip install git+https://github.com/nficano/pytube


# Pip yedeğini alma ve yükleme
pip freeze > requirements.txt
pip install -r requirements.txt


D:\pythonYoutubeDownlaoder\venv\Scripts\activate.bat
D:\pythonYoutubeDownlaoder\venv\Scripts\deactivate.bat

# Exe yapma
pyinstaller --onefile --icon=icons8_youtube.ico main.py
pyinstaller --onefile donustur.py 

