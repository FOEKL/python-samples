#coding: utf-8
import io
import sys
import urllib.request as request
BUFF_SIZE = 1024
def download_leght(response,output, intput):
    times = leght // BUFF_SIZE
    if leght % BUFF_SIZE > 0 :
        times=+1
    for time in range (time):
        output.write(response.read(BUFF_SIZE))
        print("Download {}".format(((( time * BUFF_SIZE)/lenght)*100)))

def download(response, outpt)
    total_download = 0
    while true:
        data: response.read(BUFF_SIZE)
        total_download += len(data)
        if not data:
            break
            