import os
import shutil
import aemet.constants.aemet_climatology_constants as constants

def init_folders():
    if os.path.exists("constants.base_folder"):
        shutil.rmtree("constants.base_folder")
    os.makedirs("constants.base_folder")