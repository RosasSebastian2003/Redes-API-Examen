import requests
from Crypto.Cipher import AES
from base64 import b64encode
import os

def encrypt_image(image_path, encryption_key):
    # Encrypcion en base 64
    if not os.path.exists(image_path):
        raise ValueError("Image file not found: {}".format(image_path))

    if len(encryption_key) != 32:
        print(len(encryption_key))
        raise ValueError("Invalid encryption key length (must be 32 bytes)")

    try:
        # Leer la imagen como binarios
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        # Generar un IV aleatorio
        iv = os.urandom(16) 

        # Cipher creado con la llave de encriptacion y el IV
        cipher = AES.new(encryption_key, AES.MODE_CBC, iv)

        # La imagen debe de constituir de multiplos de 16 bytes, por lo que se agrega padding
        pad_length = 16 - (len(image_data) % 16)
        padding = bytes([pad_length] * pad_length)
        padded_data = image_data + padding

        # Encryptar
        ciphertext = cipher.encrypt(padded_data)

        encrypted_data = iv + ciphertext

        # Codificar a base 64
        base64_ciphertext = b64encode(encrypted_data).decode('utf-8')

        return base64_ciphertext

    except (IOError, OSError) as e:
        print("Error reading image file:", e)
        return None
    
# Endpoint de django
django_endpoint_url = 'http://localhost:8000/decrypt-image/'

encryption_key = b'VVBI8lKHuS8O+kavwbKMMLAa2zlh2kho'  # Llave de encripcion, no cambiar
image_path = '/Users/sebastianrosasmaciel/Downloads/pp.jpg' # Ruta de la imagen a encriptar, cambiar por una ruta dentro de su computadora

try:
    encrypted_image = encrypt_image(image_path, encryption_key)
    if encrypted_image:
        print("Image encrypted successfully.")

        # Solicitud de post a el endpoint de django
        data = {'encryptedImage': encrypted_image}
        response = requests.post(django_endpoint_url, json=data)

        if response.status_code == 200:
            print("Image sent successfully. Response:", response.text)
        else:
            print("Error sending image:", response.status_code, response.text)

except ValueError as e:
    print("Error:", e)