from aemet.alerts.dtos.aemet_alert_csv_data import AemetAlertCsvData
import aemet.constants.aemet_alert_constants as constants


def extract_key_or_null(root_xml, target_key):
    try:
        return root_xml.find(target_key, namespaces=constants.alerts_xml_namespace).text
    except Exception as e:
        return f"No data available, error {e}"

def extract_csv_data_from_xml(root_xml):
    alert_type = root_xml.find(constants.type, namespaces=constants.alerts_xml_namespace).text

    try:
        severity = extract_key_or_null(root_xml, constants.severity_key)
        sent = extract_key_or_null(root_xml, constants.sent_key)
        effective = extract_key_or_null(root_xml, constants.effective_key)
        event = extract_key_or_null(root_xml, constants.event_key)
        description = extract_key_or_null(root_xml, constants.description_key)
        area = extract_key_or_null(root_xml, constants.area_key)
        alert_type = extract_key_or_null(root_xml, constants.type)
    except Exception as e:
        print(f"alert_type: {alert_type}, error: {e}")

    return AemetAlertCsvData(
        severity=severity,
        sent=sent,
        effective=effective,
        event=event,
        description=description,
        area=area,
        alert_type=alert_type
    )

if __name__ == "__main__":
    extract_csv_data_from_xml("")