import subprocess
import threading
import os

folder="test_files"

def upload(file):

    subprocess.run([
        "shelby",
        "upload",
        f"{folder}/{file}",
        f"stress/{file}"
    ])

threads=[]

for file in os.listdir(folder):

    t=threading.Thread(target=upload,args=(file,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Stress test complete")