import csv
import os
import aemet.components.aemet_constants as constants
import aemet.components.aemet_alert_extractor as csv_data_extractor
import xml.etree.ElementTree as ET

results_folder = constants.aemet_analysis_results_folder
results_file_name = "-aemet-alerts.csv"
fields_stored = ["severity", "area", "sent", "effective", "event", "description", "alert_type"]

def write_aemet_alert_report(target_folder, target_alert):
    lowercase_alert = target_alert.lower()
    csv_file = results_folder + "\\" + lowercase_alert + results_file_name

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields_stored, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for root, _, files in os.walk(target_folder):
            for file in files:
                if file.endswith(".xml"):
                    archivo_xml = os.path.join(root, file)
                    try:
                        tree = ET.parse(archivo_xml)
                        root_xml = tree.getroot()

                        row_data = csv_data_extractor.extract_csv_data_from_xml(root_xml)

                        writer.writerow(vars(row_data))

                    except ET.ParseError:
                        print(f"Error parsing xml file: {archivo_xml}")
                    except Exception as e:
                        print(f"Error processing file {archivo_xml}: {e}")
    print(f"Analyzed alert for level: {target_alert}")

if __name__ == "__main__":
    write_aemet_alert_report(constants.extreme_aemet_alert_folder, constants.extreme_alert_level)
    write_aemet_alert_report(constants.severe_aemet_alert_folder, constants.severe_alert_level)
    write_aemet_alert_report(constants.moderate_aemete_alert_folder, constants.moderate_alert_level)
    write_aemet_alert_report(constants.minor_aemet_alert_folder, constants.minor_alert_level)
