from pytube import YouTube
import os

# url 
yt = YouTube(input("URL: "))


# audio
video = yt.streams.filter(only_audio=True).first()

# destino
destination = "C:\Música" #C:\Música

# descarga
out_file = video.download(output_path=destination)

# guardado
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# resultado
print(yt.title + " se ha descargado correctamente.")