import os
import requests
from tqdm import tqdm

API_KEY = 'd05642ed-f26a-499d-a4d7-df5a99e7e83c'
UPLOAD_URL = 'https://pixeldrain.com/api/file'
FOLDER_URL = 'https://pixeldrain.com/api/folder'

headers = {'Authorization': f'Bearer {API_KEY}'}

def upload_file(filepath):
    filesize = os.path.getsize(filepath)
    with open(filepath, 'rb') as f, tqdm(total=filesize, unit='B', unit_scale=True, desc=os.path.basename(filepath)) as pbar:
        def progress(monitor):
            pbar.update(monitor.bytes_read - pbar.n)

        files = {'file': (os.path.basename(filepath), f)}
        response = requests.post(UPLOAD_URL, files=files, headers=headers)
    if response.status_code == 200:
        url = response.json()['url']
        print(f'Uploaded {filepath} → {url}')
        return url
    else:
        print(f'Failed to upload {filepath}:', response.text)
        return None

def upload_folder(folderpath):
    urls = []
    for root, _, files in os.walk(folderpath):
        for file in files:
            fullpath = os.path.join(root, file)
            urls.append(upload_file(fullpath))
    return urls

def get_user_folder_choice():
    print("PixelDrain doesn't officially support nested folders in API, so we fake it with naming.")
    print("Do you want to:")
    print("1. Create a new folder name prefix for your files")
    print("2. Use an existing folder name prefix (just a name, not real folders)")
    choice = input("Choose 1 or 2: ").strip()
    folder_name = ""
    if choice == '1':
        folder_name = input("Enter new folder name: ").strip()
    elif choice == '2':
        folder_name = input("Enter existing folder name: ").strip()
    return folder_name

def main():
    path = input("Enter file or folder path to upload: ").strip()
    if not os.path.exists(path):
        print("Bruh, that path doesn’t exist.")
        return

    folder_prefix = get_user_folder_choice()

    if os.path.isfile(path):
        urls = [upload_file(path)]
    else:
        urls = upload_folder(path)

    # Add folder prefix to URLs to “simulate” folders in the output
    if folder_prefix:
        print("\nYour files under folder:", folder_prefix)
        for url in urls:
            if url:
                print(f"{folder_prefix}/{url.split('/')[-1]} -> {url}")
    else:
        print("\nYour uploaded files:")
        for url in urls:
            if url:
                print(url)

if __name__ == '__main__':
    main()
