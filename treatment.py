import requests
import time

url = 'http://127.0.0.1:5000/'
wordlist_path = './dir_list.txt'
directory_list = []

# Open the wordlist and read the contents
with open(wordlist_path, "r") as f:
    wordlist = f.read().splitlines()

start_time = time.time()  # Start timer

# Loop through each directory in the wordlist and send a request to the URL
for directory in wordlist:
    directory_url = url + "/" + directory
    print("testing " + directory_url)
    response = requests.get(directory_url)
    if response.status_code == 200:
        directory_list.append(directory_url)

# Stop timer and calculate duration
end_time = time.time()
duration = end_time - start_time

for avalaible_directory in directory_list:
    print("[+] Found directory:", avalaible_directory)

# Print treatment duration
print("Treatment duration:", duration, "seconds")