import os
import hashlib
import time

def calculate_file_hash(filepath):
    sha512_hash = hashlib.sha512()
    with open(filepath, "rb") as f:
        # Read the file in chunks to handle large files efficiently
        for chunk in iter(lambda: f.read(4096), b""):
            sha512_hash.update(chunk)
    return sha512_hash.hexdigest()

def erase_baseline_if_already_exists():
    baseline_file = "./baseline.txt"
    if os.path.exists(baseline_file):
        os.remove(baseline_file)

def notify_change(file_path, status):
    if status == "created":
        print(f"{file_path} has been created!")
    elif status == "changed":
        print(f"{file_path} has changed!")
    elif status == "deleted":
        print(f"{file_path} has been deleted!")

print("\nWhat would you like to do?")
print("\n    A) Collect new Baseline?")
print("    B) Begin monitoring files with saved Baseline?\n")

response = input("Please enter 'A' or 'B': ").upper()

if response == "A":
    # Delete baseline.txt if it already exists
    erase_baseline_if_already_exists()

    # Calculate Hash from the target files and store in baseline.txt
    baseline_file = "./baseline.txt"
    with open(baseline_file, "w") as f:
        for root, _, files in os.walk("./Files"):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = calculate_file_hash(file_path)
                f.write(f"{file_path}|{file_hash}\n")

elif response == "B":
    file_hash_dictionary = {}

    # Load file|hash from baseline.txt and store them in a dictionary
    baseline_file = "./baseline.txt"
    with open(baseline_file, "r") as f:
        for line in f:
            file_path, file_hash = line.strip().split("|")
            file_hash_dictionary[file_path] = file_hash

    # Dictionary to keep track of already notified changes
    notified_files = {}

    # Begin (continuously) monitoring files with saved Baseline
    while True:
        time.sleep(1)

        for root, _, files in os.walk("./Files"):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = calculate_file_hash(file_path)

                # Notify if a new file has been created
                if file_path not in file_hash_dictionary:
                    if file_path not in notified_files:
                        notify_change(file_path, "created")
                        notified_files[file_path] = "created"

                # Notify if a file has been changed
                elif file_hash_dictionary[file_path] != file_hash:
                    if file_path not in notified_files:
                        notify_change(file_path, "changed")
                        notified_files[file_path] = "changed"

        # Check for deleted files in the baseline
        for file_path in list(file_hash_dictionary.keys()):
            if not os.path.exists(file_path):
                if file_path not in notified_files:
                    notify_change(file_path, "deleted")
                    notified_files[file_path] = "deleted"
                del file_hash_dictionary[file_path]
