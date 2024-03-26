import base64

encoded_script = ""

# Decode
decoded_script = base64.b64decode(encoded_script.encode())
print(decoded_script.decode())