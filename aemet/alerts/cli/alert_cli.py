import os
import click
from aemet.alerts.components.alert_folder_initializer import validate_paths
from aemet.alerts.operations.archive_alert_download import get_alerts_targz
from aemet.common.operations.aemet_extractor import extract_aemet_response
from aemet.alerts.operations.write_csv import write_aemet_alert_report
from aemet.common.components.find_latest_modified_folder import get_last_modified_folder
from aemet.common.components.folder_param_choice import FolderParamChoice
import aemet.constants.aemet_constants as constants

base_data_folder = constants.base_data_folder
alerts_responses_base_folder = constants.alerts_responses_path
alerts_results_base_path = constants.alerts_results_path

@click.group()
def alert():
    pass

@alert.command()
@click.argument("start_date")
@click.argument("end_date")
def download_alert_archive(start_date, end_date):
    validate_paths()
    if not start_date.endswith("UTC"):
        start_date += "UTC"
    if not end_date.endswith("UTC"):
        end_date += "UTC"
    get_alerts_targz(start_date, end_date)

@alert.command()
def list_responses():
    validate_paths()
    print(os.listdir(alerts_responses_base_folder))

@alert.command()
@click.argument(
    "date_folder",
    required=False,
    default="LATEST",
    type=FolderParamChoice(base_folder=alerts_responses_base_folder))
def extract_alert_archive(date_folder):
    validate_paths()
    if date_folder == "LATEST":
        date_folder = get_last_modified_folder(alerts_responses_base_folder)
    # that target_base_path should be something like ...alerts/date_n/
    target_folder = os.path.join(
        alerts_responses_base_folder,
        date_folder
    )
    extract_aemet_response(target_folder)

@alert.command()
@click.argument(
    "date_folder",
    required=False,
    default="LATEST",
    type=FolderParamChoice(base_folder=alerts_responses_base_folder))
def write_csv(date_folder):
    validate_paths()
    if date_folder == "LATEST":
        date_folder = get_last_modified_folder(alerts_responses_base_folder)
    # that target_base_path should be something like ...alerts/responses/date_n/
    origin_folder = os.path.join(
        alerts_responses_base_folder,
        date_folder
    )
    if not os.path.exists(alerts_results_base_path):
        os.mkdir(alerts_results_base_path)
    target_folder = os.path.join(
        alerts_results_base_path,
        date_folder
    )
    if not os.path.exists(target_folder):
        os.mkdir(target_folder)
    if not os.path.exists(origin_folder):
        print(f"Unrecognized response folder {origin_folder}")
        pass
    write_aemet_alert_report(origin_folder, target_folder)
