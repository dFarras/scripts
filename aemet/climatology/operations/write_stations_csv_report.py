import csv
import os
import json
from aemet.climatology.dto.aemet_station import AemetStation
import aemet.constants.aemet_constants as constants
import aemet.constants.aemet_stations_constants as stations_constants

fields_stored = ["latitude", "province", "altitude", "indicative", "name", "indsinop", "longitude"]

#that origin_folder should be something like ...alerts/responses/date_n/
#that target_folder should be something like ...alerts/results/date_n/
def write_aemet_stations_report(origin_folder, target_folder):
    file_to_read = os.path.join(
        origin_folder,
        constants.responses_downloaded_folder,
        stations_constants.stations_response_file_name)
    csv_file = os.path.join(
        target_folder,
        stations_constants.stations_csv_file_name)

    with open(csv_file, mode='w', newline='', encoding='utf-8') as csv_station_file:
        writer = csv.DictWriter(csv_station_file, fieldnames=fields_stored, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        with open(file_to_read, "r") as file:
            json_data = json.load(file)
            locations = [AemetStation(**item) for item in json_data]
            for location in locations:
                writer.writerow(vars(location))
