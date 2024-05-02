from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from Crypto.Cipher import AES 
import base64

import numpy
import tempfile

def decrypt_image(encrypted_image_data, encryption_key):
    # Assuming the encrypted_image_data is base64 encoded
    encrypted_image_data = base64.b64decode(encrypted_image_data)

    # Assuming the encryption_key is a string of 32 bytes
    cipher = AES.new(encryption_key.encode(), AES.MODE_ECB)
    decrypted_image_data = cipher.decrypt(encrypted_image_data)

    return decrypted_image_data

@csrf_exempt
def decrypt_image_view(request):
    if request.method == 'POST':
        encrypted_image_data = request.POST['encryptedImage']
        encryption_key = 'VVBI8lKHuS8O+kavwbKMMLAa2zlh2kho'
        decrypted_image_data = decrypt_image(encrypted_image_data, encryption_key)

        # Continue with your image processing...
    else:
        return JsonResponse({'error': 'Invalid request method'})