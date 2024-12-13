import requests
from aemet.constants.secrets.aemet import api_key as aemet_api_key
import aemet.constants.aemet_alert_constants as constants
from aemet.common.dtos.aemet_hateoas_response import AemetHateoasResponse

api_key = aemet_api_key
base_url = "https://opendata.aemet.es/opendata"
output_file = "{constants.response_folder}\\aemet-alerts.gtar"

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

def get_aemet_station_hateoas_url():
    stations_url = f"{base_url}/api/valores/climatologicos/inventarioestaciones/todasestaciones"
    response = requests.get(stations_url, headers=headers, params=params)

    if response.status_code == 200:
        json_data = response.json()
        aemet_hateoas = map_response(json_data)
        return aemet_hateoas
    else:
        print(f"Request failed with status code: {response.status_code}")

def download_alerts_from_hateoas_url(url):
    try:
        with requests.get(url, stream=True, params=params) as response:
            if response.status_code == 200:
                with open(output_file, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
            else:
                print(f"Failed to download file: {response.status_code} - {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")