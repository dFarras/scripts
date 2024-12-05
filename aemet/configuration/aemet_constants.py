import os

home_folder = os.environ.get("HOME") or os.environ.get("USERPROFILE")
base_folder = f"{home_folder}\\PycharmProjects\\scripts\\data"

# Were targz from aemet response will be stored
aemet_response_folder = f"{base_folder}\\response"
aemet_decompressed_response_folder = aemet_response_folder + "\\decompressed"
# Folder were all transformations to aemet data will be
filtered_response_folder = f"{base_folder}\\filtered"
# Folder containing the human-readable result of the analysis
aemet_analysis_results_folder = f"{base_folder}\\results"

# Folders were aemet alert xmls will be stored after extraction from aemet_response_folder and classification
raw_alerts_destination_folder = filtered_response_folder + "\\raw"
extreme_aemet_alert_folder = filtered_response_folder + "\\extreme"
severe_aemet_alert_folder = filtered_response_folder + "\\severe"
moderate_aemete_alert_folder = filtered_response_folder + "\\moderate"
minor_aemet_alert_folder = filtered_response_folder + "\\minor"
unknown_aemet_folder = filtered_response_folder + "\\unknown"

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
aemet_xml_namespace = {'ns': 'urn:oasis:names:tc:emergency:cap:1.2'}
