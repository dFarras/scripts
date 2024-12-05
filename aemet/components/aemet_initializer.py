import os
import shutil
import aemet.configuration.aemet_constants as constants

def init_folders():
    print("Starting folder initialization")
    if not os.path.exists(constants.base_folder):
        os.makedirs(constants.base_folder)
    else:
        print("Previous run detected. Deleting old execution data folder")
        shutil.rmtree(constants.base_folder)
        os.makedirs(constants.base_folder)

    print(f"Creating data folders on base folder: {constants.base_folder}")
    os.makedirs(constants.aemet_response_folder)
    os.makedirs(constants.aemet_decompressed_response_folder)
    os.makedirs(constants.filtered_response_folder)
    os.makedirs(constants.aemet_analysis_results_folder)

    os.makedirs(constants.raw_alerts_destination_folder)
    os.makedirs(constants.extreme_aemet_alert_folder)
    os.makedirs(constants.severe_aemet_alert_folder)
    os.makedirs(constants.moderate_aemete_alert_folder)
    os.makedirs(constants.minor_aemet_alert_folder)
    os.makedirs(constants.unknown_aemet_folder)

if __name__ == "__main__":
    init_folders()