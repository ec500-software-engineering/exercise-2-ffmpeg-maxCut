import shutil 
import sys
import subprocess
import threading

br = 30
fps = 60

def analyze(resolution, name):
    print("here")
    fout = str(resolution) + ".mp4"
    subprocess.call(["ffmpeg", "-i",str(name),"-b:v",
            str(br)+"M","-r",str(fps),"-s","hd" + str(resolution),str(fout)])

def main():
    fileName = sys.argv[1]
    print(fileName)

    threads = []
    for res in ["480", "720"]:
        thr=threading.Thread(target=analyze,args=(res,fileName,))
        threads.append(thr)
        thr.start()

    for tr in threads:
        tr.join()

main()
