import base64

# Encode
with open("keylogger.py", "rb") as script_file:
    encoded_script = base64.b64encode(script_file.read())
    
with open("encoder/encoded_keylogger.py", "wb") as encoded_file:
    encoded_file.write(encoded_script)