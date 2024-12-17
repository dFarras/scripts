import os
import requests
from datetime import datetime
from aemet.constants.secrets.aemet import api_key as aemet_api_key
from aemet.common.dtos.aemet_hateoas_response import AemetHateoasResponse
import aemet.constants.aemet_stations_constants as stations_constants
import aemet.constants.aemet_constants as constants

api_key = aemet_api_key
base_url = "https://opendata.aemet.es/opendata"
output_folder = constants.stations_responses_path
download_folder = constants.responses_downloaded_folder
output_file = stations_constants.stations_response_file_name

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

def request_aemet_stations_hateoas_url():
    stations_path = f"{base_url}/api/valores/climatologicos/inventarioestaciones/todasestaciones"
    response = requests.get(stations_path, headers=headers, params=params)

    if response.status_code == 200:
        json_data = response.json()
        aemet_hateoas = map_response(json_data)
        return aemet_hateoas
    else:
        print(f"Request failed with status code: {response.status_code}")

def init_folder(date_folder):
    os.mkdir(os.path.join(output_folder, date_folder).__str__())
    os.mkdir(os.path.join(output_folder, date_folder, download_folder))

def download_stations_from_hateoas_url(url):
    datetime_now = datetime.now()
    folder_name = datetime_now.strftime("%Y-%m-%d_%H-%M-%S")
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

def download_all_stations():
    response = request_aemet_stations_hateoas_url()
    print(response.__str__())
    download_stations_from_hateoas_url(response.data)

if __name__ == "__main__":
    download_all_stations()