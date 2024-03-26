import base64

# Encode
with open("keylogger.py", "rb") as script_file:
    encoded_script = base64.b64encode(script_file.read())
    
with open("encoder/encoded_keylogger.py", "wb") as encoded_file:
    encoded_file.write(encoded_script)
    

# Decode
decoded_script = base64.b64decode(encoded_script)

# Sauvegarde du code decodé
with open("encoder/decoded_keylogger.py", "wb") as decoded_file:
    decoded_file.write(decoded_script)