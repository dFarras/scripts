import os

#Configuration files
home_folder = os.environ.get("HOME") or os.environ.get("USERPROFILE")
configuration_folder = os.path.join(home_folder, ".aemet-cli")
configuration_file = "configuration"
base_data_folder = os.path.join(home_folder, "aemet")

#Aemet data
base_url = "https://opendata.aemet.es/opendata"

#Modules available
alerts_folder = "alerts"
stations_folder = "climatology-stations"
climatology_folder = "climatology"

#Common folder structure
#Everything inside the base folder
responses_base_relative_path = "response"
results_base_relative_path = "results"

#Module base path
alerts_base_path = os.path.join(base_data_folder, alerts_folder)
stations_base_path = os.path.join(base_data_folder, stations_folder)
climatology_base_path = os.path.join(base_data_folder, climatology_folder)

#Module inner paths
alerts_responses_path = os.path.join(base_data_folder, alerts_folder, responses_base_relative_path)
alerts_results_path = os.path.join(base_data_folder, alerts_folder, results_base_relative_path)
stations_responses_path = os.path.join(base_data_folder, stations_folder, responses_base_relative_path)
stations_results_path = os.path.join(base_data_folder, stations_folder, results_base_relative_path)
climatology_responses_path = os.path.join(base_data_folder, climatology_folder, responses_base_relative_path)

#Path usages pattern {xxxxxx_response_path}\\date_n\\{responses_blablabla_folder}
responses_downloaded_folder = "downloaded"
responses_unpacked_folder = "unpacked"
responses_decompressed_folder = "decompressed"