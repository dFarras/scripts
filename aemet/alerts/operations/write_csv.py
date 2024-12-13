import csv
import os
import aemet.constants.aemet_constants as constants
import aemet.constants.aemet_alert_constants as alerts_constants
import aemet.alerts.components.aemet_alert_extractor as csv_data_extractor
import xml.etree.ElementTree as ElementTree

fields_stored = ["severity", "area", "sent", "effective", "event", "description", "alert_type"]

#that origin_folder should be something like ...alerts/responses/date_n/
#that target_folder should be something like ...alerts/results/date_n/
def write_aemet_alert_report(origin_folder, target_folder):
    files_to_read = os.path.join(
        origin_folder,
        constants.responses_decompressed_folder)
    csv_file = os.path.join(
        target_folder,
        alerts_constants.alerts_archive_csv_file_name)

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields_stored, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for root, _, files in os.walk(files_to_read.__str__()):
            for file in files:
                if file.endswith(".xml"):
                    archivo_xml = os.path.join(root, file)
                    try:
                        tree = ElementTree.parse(archivo_xml)
                        root_xml = tree.getroot()

                        row_data = csv_data_extractor.extract_csv_data_from_xml(root_xml)

                        writer.writerow(vars(row_data))

                    except ElementTree.ParseError:
                        print(f"Error parsing xml file: {archivo_xml}")
                    except Exception as e:
                        print(f"Error processing file {archivo_xml}: {e}")
