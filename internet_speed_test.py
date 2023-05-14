import speedtest
#pip install speedtest-cli

def bytes_to_mb(bytes):
  KB = 1024 
  MB = KB * 1024
  return int(bytes/MB)

speed_test = speedtest.Speedtest()

download_speed = speed_test.download()
print( "Velocidad de descarga: ", bytes_to_mb(download_speed), " Mbps")

upload_speed = speed_test.upload()
print( "Velocidad de subida: ", bytes_to_mb(upload_speed), " Mbps")
