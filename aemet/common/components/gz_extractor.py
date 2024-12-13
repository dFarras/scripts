import os
import tarfile

def uncompress_response(gz_files_folder, destination_folder):
    if not os.path.exists(gz_files_folder):
        print(f"Could not find any response at {gz_files_folder}")
    for root, _, files in os.walk(gz_files_folder):
        for file in files:
            if file.endswith(".gz"):
                try:
                    with tarfile.open(os.path.join(root, file), "r:gz") as tar:
                        tar.extractall(path=destination_folder)
                except FileNotFoundError:
                    print(f"Error: File '{file}' not found.")
                except tarfile.TarError as e:
                    print(f"Error extracting the tar.gz file: {e}")
                except PermissionError as e:
                    print(f"PermissionError: {e}")
