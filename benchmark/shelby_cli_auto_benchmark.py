import subprocess
import time
import csv
import os

RESULT_FILE = "results/benchmark_results.csv"
TEST_FILE = "testfile.bin"
FILE_SIZE_MB = 10


def generate_test_file():
    if not os.path.exists(TEST_FILE):
        print("Generating test file...")
        with open(TEST_FILE, "wb") as f:
            f.write(os.urandom(FILE_SIZE_MB * 1024 * 1024))


def run_command(cmd):
    start = time.time()
    process = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    end = time.time()

    duration = end - start

    if process.returncode != 0:
        print("Command error:", process.stderr)

    return duration, process.stdout, process.stderr


def benchmark_upload():
    print("Running upload benchmark...")

    cmd = f"shelby upload {TEST_FILE}"

    duration, out, err = run_command(cmd)

    throughput = FILE_SIZE_MB / duration if duration > 0 else 0

    print(out)

    return {
        "operation": "upload",
        "file_size_mb": FILE_SIZE_MB,
        "time_sec": duration,
        "throughput_mb_s": throughput
    }


def benchmark_download(cid):
    print("Running download benchmark...")

    filename = f"downloaded_{int(time.time())}.bin"

    cmd = f"shelby download {cid} {filename}"

    duration, out, err = run_command(cmd)

    throughput = FILE_SIZE_MB / duration if duration > 0 else 0

    print(out)

    return {
        "operation": "download",
        "file_size_mb": FILE_SIZE_MB,
        "time_sec": duration,
        "throughput_mb_s": throughput
    }


def save_result(result):

    os.makedirs("results", exist_ok=True)

    file_exists = os.path.isfile(RESULT_FILE)

    with open(RESULT_FILE, "a", newline="") as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=result.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(result)


def main():

    generate_test_file()

    upload_result = benchmark_upload()

    save_result(upload_result)

    print("Upload result:", upload_result)

    print("Enter CID returned from upload:")

    cid = input("> ")

    download_result = benchmark_download(cid)

    save_result(download_result)

    print("Download result:", download_result)


if __name__ == "__main__":
    main()