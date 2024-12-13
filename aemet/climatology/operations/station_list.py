import os
import requests
from datetime import datetime
from aemet.constants.secrets.aemet import api_key as aemet_api_key
import aemet.constants.aemet_alert_constants as constants
from aemet.common.dtos.aemet_hateoas_response import AemetHateoasResponse

api_key = aemet_api_key
base_url = "https://opendata.aemet.es/opendata"
conf_start_date = "2024-11-29T00:00:01UTC"
conf_end_date = "2024-11-29T23:59:59UTC"
output_folder = "{constants.response_folder}"
output_file = constants.alerts_response_file_name

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
    alerts_path = f"/api/valores/climatologicos/inventarioestaciones/todasestaciones"
    response = requests.get(alerts_path, headers=headers, params=params)

    if response.status_code == 200:
        json_data = response.json()
        aemet_hateoas = map_response(json_data)
        return aemet_hateoas
    else:
        print(f"Request failed with status code: {response.status_code}")

def download_stations_from_hateoas_url(url):
    datetime_now = datetime.now()
    now_str = datetime_now.strftime("%Y-%m-%d_%H-%M-%S")
    output_download_file = os.path.join(output_folder, now_str, output_file)
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
    download_stations_from_hateoas_url(response.data)

if __name__ == "__main__":
    download_all_stations()