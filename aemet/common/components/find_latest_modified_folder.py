import os


def get_last_modified_folder(path):
    folders = [os.path.join(path, folder) for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]

    if not folders:
        print("platirinchus")
        return None

    last_modified_folder = max(folders, key=os.path.getmtime)

    print(os.path.basename(last_modified_folder).__str__())
    return os.path.basename(last_modified_folder)

def get_folders_order_by_last_modified(path):
    entries = os.scandir(path)

    # Filter directories and get their modification times
    dirs_with_mod_time = [
        (entry, entry.stat().st_mtime)
        for entry in entries if entry.is_dir()
    ]

    # Sort directories by modification time (latest first)
    return dirs_with_mod_time.sort(key=lambda x: x[1], reverse=True)
