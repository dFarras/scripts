import os
import click
from aemet.common.operations.aemet_extractor import extract_aemet_response
from aemet.climatology.operations.station_list import download_all_stations
from aemet.common.components.folder_param_choice import FolderParamChoice
from aemet.common.components.find_latest_modified_folder import get_last_modified_folder
import aemet.constants.aemet_climatology_constants as climatology_constants
import aemet.constants.aemet_constants as constants

climatology_base_folder = os.path.join(constants.base_data_folder, climatology_constants.climatology_base_folder_name).__str__()

@click.group()
def climatology():
    pass

@climatology.command()
def download_station_list():
    download_all_stations()

@climatology.command()
def list_stations():
    print(os.listdir(climatology_base_folder))

@climatology.command()
@click.argument(
    "date_folder",
    required=False,
    default="LATEST",
    type=FolderParamChoice(base_folder=climatology_base_folder))
def extract_climatology_archive(date_folder):
    if date_folder == "LATEST":
        date_folder = get_last_modified_folder(climatology_base_folder)
    # that target_base_path should be something like ...alerts/date_n/
    target_folder = os.path.join(
        climatology_base_folder.__str__(),
        date_folder
    )
    if not os.path.exists(target_folder):
        print(f"Unrecognized response folder {target_folder}")
        pass
    extract_aemet_response(target_folder)

@climatology.command()
@click.argument(
    "date_folder",
    required=False,
    default="LATEST",
    type=FolderParamChoice(base_folder=climatology_base_folder))
def write_csv(date_folder):
    print("Work in progress")
