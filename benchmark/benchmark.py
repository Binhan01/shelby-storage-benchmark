import subprocess
import time
import os
import csv

folder = "test_files"

results = []

for file in os.listdir(folder):

    local = f"{folder}/{file}"
    remote = f"benchmark/{file}"

    start = time.time()

    subprocess.run(["shelby","upload",local,remote])

    upload = time.time() - start

    start = time.time()

    subprocess.run(["shelby","download",remote,f"download_{file}"])

    download = time.time() - start

    results.append([file,upload,download])

with open("results/benchmark_results.csv","w",newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["file","upload_time","download_time"])
    writer.writerows(results)

print("Benchmark finished")