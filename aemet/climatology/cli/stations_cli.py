import os
import click
from aemet.climatology.components.stations_folder_initializer import validate_paths
from aemet.climatology.operations.station_list_download import download_all_stations
from aemet.common.components.folder_param_choice import FolderParamChoice
from aemet.common.components.find_latest_modified_folder import get_last_modified_folder
from aemet.climatology.operations.write_stations_csv_report import write_aemet_stations_report
import aemet.constants.aemet_constants as constants
import aemet.constants.aemet_stations_constants as stations_constants

stations_base_folder = constants.stations_responses_path
stations_response_file_name = stations_constants.stations_response_file_name
stations_results_base_path = constants.stations_results_path

@click.group()
def stations():
    pass

@stations.command(name="download")
def download_station_list():
    validate_paths()
    download_all_stations()

@stations.command(name="list")
def list_stations():
    validate_paths()
    print(os.listdir(stations_base_folder))

@stations.command(name="csv")
@click.argument(
    "date_folder",
    required=False,
    default="LATEST",
    type=FolderParamChoice(base_folder=stations_base_folder))
def write_csv(date_folder):
    validate_paths()
    if date_folder == "LATEST":
        date_folder = get_last_modified_folder(stations_base_folder)
    # that target_base_path should be something like ...alerts/responses/date_n/
    origin_folder = os.path.join(
        stations_base_folder,
        date_folder
    )
    if not os.path.exists(stations_results_base_path):
        os.mkdir(stations_results_base_path)
    target_folder = os.path.join(
        stations_results_base_path,
        date_folder
    )
    if not os.path.exists(target_folder):
        os.mkdir(target_folder)
    if not os.path.exists(origin_folder):
        print(f"Unrecognized response folder {origin_folder}")
        pass
    write_aemet_stations_report(origin_folder, target_folder)
