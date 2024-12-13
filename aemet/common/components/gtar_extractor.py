import os
import tarfile

def unpack_response(gtar_file, destination_folder):
    if not os.path.exists(gtar_file):
        print(f"Could not find any response at {gtar_file}")
    try:
        with tarfile.open(gtar_file, "r") as tar:
            tar.extractall(path=destination_folder)
    except FileNotFoundError:
        print(f"File not found.")
    except tarfile.TarError as e:
        print(f"An error occurred while extracting the file: {e}")
