import os
import aemet.constants.aemet_constants as constants

base_folder = os.path.join(constants.base_data_folder, "alerts")

alerts_base_folder_name = "alerts"

alerts_response_file_name = "aemet-alerts.gtar"
alerts_archive_csv_file_name = "alerts_archive.csv"

# Aemet known alert levels
extreme_alert_level = "Extreme"
severe_alert_level = "Severe"
moderate_alert_level = "Moderate"
minor_alert_level = "Minor"

# Aemet target keys
severity_key = ".//ns:severity"
sent_key = ".//ns:sent"
effective_key = ".//ns:effective"
event_key = ".//ns:event"
description_key = ".//ns:description"
area_key = ".//ns:areaDesc"
type = ".//ns:info/ns:eventCode/ns:value"

# Aemet xml namespace
alerts_xml_namespace = {'ns': 'urn:oasis:names:tc:emergency:cap:1.2'}
