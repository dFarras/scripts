import os
import aemet.constants.aemet_constants as constants

base_data_folder = constants.base_data_folder
configuration_file_path = os.path.join(constants.configuration_folder, constants.configuration_file)

def initialize_modules():
    if not os.path.exists(constants.alerts_base_path):
        print("Initializing alerts module")
        os.mkdir(constants.alerts_base_path)
    if not os.path.exists(constants.climatology_base_path):
        print("Initializing climatology module")
        os.mkdir(constants.climatology_base_path)

def validate_paths():
    if not os.path.exists(base_data_folder):
        print("Initializing data folder")
        os.mkdir(base_data_folder)
    if not os.path.exists(constants.configuration_folder):
        print(f"Initializing aemet cli configuration at {constants.configuration_folder}")
        os.mkdir(constants.configuration_folder)
    initialize_modules()
