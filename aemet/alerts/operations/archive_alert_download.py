import os
import requests
from datetime import datetime
from aemet.constants.secrets.aemet import api_key as aemet_api_key
import aemet.constants.aemet_constants as constants
import aemet.constants.aemet_alert_constants as alert_constants
from aemet.common.dtos.aemet_hateoas_response import AemetHateoasResponse

api_key = aemet_api_key
base_url = "https://opendata.aemet.es/opendata"
conf_start_date = "2024-11-29T00:00:01UTC"
conf_end_date = "2024-11-29T23:59:59UTC"
output_folder = constants.alerts_responses_path
download_folder = constants.responses_downloaded_folder
output_file = alert_constants.alerts_response_file_name

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

params = {
    "api_key": api_key
}

def map_response(json_data):
    return AemetHateoasResponse(
        description=json_data.get("descripcion"),
        status=json_data.get("estado"),
        data=json_data.get("datos"),
        metadata=json_data.get("metadatos")
    )

def request_aemet_alerts_hateoas_url(start_date, end_date):
    alerts_path = f"{base_url}/api/avisos_cap/archivo/fechaini/{start_date}/fechafin/{end_date}"
    response = requests.get(alerts_path, headers=headers, params=params)

    if response.status_code == 200:
        json_data = response.json()
        aemet_hateoas = map_response(json_data)
        return aemet_hateoas
    else:
        print(f"Request failed with status code: {response.status_code}")

def init_folder(date_folder):
    os.mkdir(os.path.join(output_folder, date_folder).__str__())
    os.mkdir(os.path.join(output_folder, date_folder, download_folder))


def download_alerts_from_hateoas_url(url, start_date, end_date):
    datetime_now = datetime.now()
    epoch = int(datetime_now.timestamp())
    folder_name =  start_date.replace(":", "") + "-" + end_date.replace(":", "") + "-" + epoch.__str__()
    output_download_file = os.path.join(output_folder, folder_name, download_folder, output_file)
    init_folder(folder_name)
    try:
        with requests.get(url, stream=True, params=params) as response:
            if response.status_code == 200:
                with open(output_download_file, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
            else:
                print(f"Failed to download file: {response.status_code} - {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_alerts_targz(start_date, end_date):
    response = request_aemet_alerts_hateoas_url(start_date, end_date)
    print(response.__str__())
    download_alerts_from_hateoas_url(response.data, start_date, end_date)

if __name__ == "__main__":
    get_alerts_targz(conf_start_date, conf_end_date)