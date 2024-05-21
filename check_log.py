#!/usr/bin/env python3

import subprocess
import shutil
import os

def get_directory_size(directory):
    result = subprocess.run(['du', '-sh', directory], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    return result.stdout.split()[0]

def convert_to_mb(size_str):
    size_str = size_str.upper()
    if size_str.endswith('G'):
        return float(size_str[:-1]) * 1024
    elif size_str.endswith('M'):
        return float(size_str[:-1])
    elif size_str.endswith('K'):
        return float(size_str[:-1]) / 1024
    return float(size_str)

def clear_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

def main():
    log_directory = "/var/log" 
    size_str = get_directory_size(log_directory)
    if size_str is None:
        return
    
    size_mb = convert_to_mb(size_str)
    print(f"The log directory is taking {size_mb:.2f} MB of space.")
    
    if size_mb > 100:
        user_input = input("The log directory is taking more than 100MB. Do you want to clear it? (y/n): ").strip().lower()
        if user_input == 'y':
            clear_directory(log_directory)
            print("Log directory has been cleared.")
        else:
            print("Log directory has not been cleared.")
    else:
        print("Log directory size is within the limit.")

if __name__ == "__main__":
    main()
