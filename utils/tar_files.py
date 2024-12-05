import tarfile

def extract_file(file_path, destination_path):
    try:
        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(path=destination_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except tarfile.TarError as e:
        print(f"Error extracting the tar.gz file: {e}")
    except PermissionError as e:
        print(f"PermissionError: {e}")