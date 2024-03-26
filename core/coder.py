import base64

# Encode
with open("keylogger.py", "rb") as script_file:
    encoded_script = base64.b64encode(script_file.read())