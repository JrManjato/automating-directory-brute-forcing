import argparse
import requests
import threading
import time

# Function to test directories from the wordlist
def test_directories(wordlist_part, url, directory_list):
    for directory in wordlist_part:
        directory_url = url + "/" + directory
        print("testing " + directory_url)
        response = requests.get(directory_url)
        if response.status_code in [200, 403, 500]:
            directory_list.append(directory_url)

def main():
    parser = argparse.ArgumentParser(description="Directory Tester")
    parser.add_argument("url", help="URL to test directories against")
    parser.add_argument("wordlist_path", help="Path to the wordlist file")
    args = parser.parse_args()

    #Get the arguments given in the params
    url = args.url
    wordlist_path = args.wordlist_path
    directory_list = []

    # Open the wordlist and read the contents
    with open(wordlist_path, "r") as f:
        wordlist = f.read().splitlines()

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
        thread = threading.Thread(target=test_directories, args=(wordlist_part, url, directory_list))
        threads.append(thread)
        thread.start()

    # Waiting for all threads to finish
    for thread in threads:
        thread.join()

    # Stop timer and calculate duration
    end_time = time.time()
    duration = end_time - start_time

    # Printing found directories
    print("\n =============  RESULT  ===============")
    for available_directory in directory_list:
        print("[+] Found directory:", available_directory)

    # Print treatment duration
    print("\n =============  DURATION  ===============")
    print("Treatment duration:", duration, "seconds")

if __name__ == "__main__":
    main()