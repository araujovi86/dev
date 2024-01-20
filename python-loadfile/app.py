#!/opt/app-root/bin/python
import os
import time

file_folder = "/opt/app-root/bin/python/input"
loaded_files = {}

def load_files():
    for filename in os.listdir(file_folder):
        if filename.endswith(".txt") and filename not in loaded_files:
            file_path = os.path.join(file_folder, filename)
            with open(file_path, 'a') as file:
                file.write("Now the file has more content!")
            fd = os.open(file_path, os.O_RDWR)
            loaded_files[filename] = fd
            content = os.read(fd, os.path.getsize(file_path))
            print(f"File {filename} loaded into memory:", content.decode())

def watch_folder():
    while True:
        load_files()
        time.sleep(10)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    print("Watching folder for changes...")
    watch_folder()
    # This point is never reached in this script as it runs indefinitely in the watch_folder loop

