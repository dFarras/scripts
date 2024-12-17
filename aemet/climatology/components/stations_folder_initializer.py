import os
import aemet.constants.aemet_constants as constants

base_data_folder = constants.base_data_folder
stations_data_folder = constants.stations_base_path
stations_responses_base_folder = constants.stations_responses_path
alerts_results_base_path = constants.alerts_results_path

def validate_paths():
    if not os.path.exists(base_data_folder):
        print(f"Creating data folder since it was missing at: {base_data_folder}")
        os.mkdir(base_data_folder)
    if not os.path.exists(stations_data_folder):
        print(f"Creating alerts module responses folder since it was missing at: {stations_data_folder}")
        os.mkdir(stations_data_folder)
    if not os.path.exists(stations_responses_base_folder):
        print(f"Creating alerts module responses folder since it was missing at: {stations_responses_base_folder}")
        os.mkdir(stations_responses_base_folder)
