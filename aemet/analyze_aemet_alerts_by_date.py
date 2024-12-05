import aemet.configuration.aemet_constants as constants
import aemet.components.aemet_initializer as aemet_init
import aemet.components.aemet_alert_finder as aemet_alerts
import aemet.components.aemet_alert_classifier as aemet_classifier
import aemet.components.aemet_csv_writer as aemet_analyzer

# Configuration
origin_folder = constants.aemet_response_folder
destination_folder = constants.raw_alerts_destination_folder

conf_start_date = "2024-10-29T00:00:01UTC"
conf_end_date = "2024-10-29T23:59:59UTC"

def process_aemet_alerts():
    aemet_init.init_folders()
    aemet_alerts.get_alerts_targz(conf_start_date, conf_end_date)
    aemet_classifier.classify_aemet_alerts()

    aemet_analyzer.write_aemet_alert_report(constants.extreme_aemet_alert_folder, constants.extreme_alert_level)
    aemet_analyzer.write_aemet_alert_report(constants.severe_aemet_alert_folder, constants.severe_alert_level)
    aemet_analyzer.write_aemet_alert_report(constants.moderate_aemete_alert_folder, constants.moderate_alert_level)
    aemet_analyzer.write_aemet_alert_report(constants.minor_aemet_alert_folder, constants.minor_alert_level)

if __name__ == "__main__":
    process_aemet_alerts()