import requests
from configuration.secrets.AemetApiKey import aemet_api_key
import aemet.components.aemet_constants as constants
from aemet.dtos.aemet_hateoas_response import AemetHateoasResponse

api_key = aemet_api_key
base_url = "https://opendata.aemet.es/opendata"
conf_start_date = "2024-11-29T00:00:01UTC"
conf_end_date = "2024-11-29T23:59:59UTC"
output_file = f"{constants.aemet_response_folder}\\aemet-alerts.gtar"

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

def get_alerts_targz(start_date, end_date):
    response = request_aemet_alerts_hateoas_url(start_date, end_date)
    print(f"Got resource url: {response}")
    download_alerts_from_hateoas_url(response.data)
    print("Downloaded alerts tar successfully")

if __name__ == "__main__":
    get_alerts_targz(conf_start_date, conf_end_date)