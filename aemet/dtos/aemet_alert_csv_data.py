
class AemetAlertCsvData:
    def __init__(self, severity, sent, effective, event, description, area, alert_type):
        self.severity = severity
        self.sent = sent
        self.effective = effective
        self.event = event
        self.description = description
        self.area = area
        self.alert_type = alert_type

    def __repr__(self):
        return f"AemetHateoasResponse(severity={self.severity}, sent={self.sent}, effective={self.effective}, event={self.event}, description={self.description}, area={self.area}, type={self.alert_type})"
