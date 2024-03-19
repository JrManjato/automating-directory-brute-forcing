import requests
import threading
import time

url = 'http://127.0.0.1:5000/'
wordlist_path = './dir_list.txt'
directory_list = []

# Open the wordlist and read the contents
with open(wordlist_path, "r") as f:
    wordlist = f.read().splitlines()

# Function to test directories from the wordlist
def test_directories(wordlist_part):
    for directory in wordlist_part:
        directory_url = url + "/" + directory
        print("testing " + directory_url)
        response = requests.get(directory_url)
        if response.status_code in [200, 403, 500]:
            directory_list.append(directory_url)

# Splitting the wordlist into three equal parts
wordlist_length = len(wordlist)
part_length = wordlist_length // 3

# Creating threads for each part of the wordlist
threads = []
start_time = time.time()  # Start timer
for i in range(3):
    start_index = i * part_length
    end_index = (i + 1) * part_length if i < 2 else wordlist_length
    wordlist_part = wordlist[start_index:end_index]
    thread = threading.Thread(target=test_directories, args=(wordlist_part,))
    threads.append(thread)
    thread.start()

# Waiting for all threads to finish
for thread in threads:
    thread.join()

# Stop timer and calculate duration
end_time = time.time()
duration = end_time - start_time

# Printing found directories
for available_directory in directory_list:
    print("[+] Found directory:", available_directory)

# Print treatment duration
print("Treatment duration:", duration, "seconds")