import os
import aemet.constants.aemet_constants as constants

base_data_folder = constants.base_data_folder
alerts_responses_base_folder = constants.alerts_responses_path
alerts_results_base_path = constants.alerts_results_path

def validate_paths():
    if not os.path.exists(base_data_folder):
        print(f"Creating data folder since it was missing at: {base_data_folder}")
        os.mkdir(base_data_folder)
    if not os.path.exists(alerts_responses_base_folder):
        print(f"Creating alerts module responses folder since it was missing at: {alerts_responses_base_folder}")
        os.mkdir(alerts_responses_base_folder)
    if not os.path.exists(alerts_results_base_path):
        print(f"Creating alerts module results folder since it was missing at: {alerts_results_base_path}")
        os.mkdir(alerts_results_base_path)