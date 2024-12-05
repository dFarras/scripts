import os
import shutil
import tarfile
import aemet.configuration.aemet_constants as constants
import xml.etree.ElementTree as ET
import utils.tar_files as tarfiles

# Configuration
origin_folder = constants.aemet_response_folder
destination_folder = constants.filtered_response_folder
raw_compressed_response_folder = constants.aemet_decompressed_response_folder
raw_decompressed_response_folder = constants.raw_alerts_destination_folder

def count_files(folder_path):
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def extract_response():
    for root, _, files in os.walk(origin_folder):
        for file in files:
            if file.endswith(".gtar"):
                try:
                    with tarfile.open(os.path.join(root, file), "r") as tar:
                        tar.extractall(path=raw_compressed_response_folder)
                        print(f"Extracted response from path: {file}")
                except FileNotFoundError:
                    print(f"File not found.")
                except tarfile.TarError as e:
                    print(f"An error occurred while extracting the file: {e}")

def extract_alerts():
    for root, _, files in os.walk(raw_compressed_response_folder):
        for file in files:
            if file.endswith(".gz"):
                filename = os.path.join(root, file)
                tarfiles.extract_file(filename, constants.raw_alerts_destination_folder)
    total_files = count_files(raw_decompressed_response_folder)
    print(f"Decompressed alerts successfully. Total alerts: {len(total_files)}")


def classify_aemet_alerts():
    extract_response()
    extract_alerts()

    total_classified_files = 0
    failed_classified_files = 0
    for root, _, files in os.walk(constants.raw_alerts_destination_folder):
        for file in files:
            if file.endswith(".xml"):
                archivo_xml = os.path.join(root, file)
                try:
                    tree = ET.parse(archivo_xml)
                    root_xml = tree.getroot()

                    alert_level = root_xml.find(constants.severity_key, namespaces=constants.aemet_xml_namespace)
                    if alert_level.text == "Minor":
                        shutil.copy(archivo_xml, constants.minor_aemet_alert_folder)
                        total_classified_files += 1
                    elif alert_level.text == "Moderate":
                        shutil.copy(archivo_xml, constants.moderate_aemete_alert_folder)
                        total_classified_files += 1
                    elif alert_level.text == "Severe":
                        shutil.copy(archivo_xml, constants.severe_aemet_alert_folder)
                        total_classified_files += 1
                    elif alert_level.text == "Extreme":
                        shutil.copy(archivo_xml, constants.extreme_aemet_alert_folder)
                        total_classified_files += 1
                    else:
                        shutil.copy(archivo_xml, constants.unknown_aemet_folder)
                        failed_classified_files += 1

                except ET.ParseError:
                    print(f"Error parsing xml file: {archivo_xml}")
                except Exception as e:
                    print(f"Error processing file {archivo_xml}: {e}")
    print(f"Alert classification finished. Files classified successfully: {total_classified_files}, Files classified wrongfully: {failed_classified_files}")

if __name__ == "__main__":
    classify_aemet_alerts()
