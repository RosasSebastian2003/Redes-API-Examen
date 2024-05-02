from PIL import Image
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .utils import decrypt_image
import numpy as np
import json
from django.utils.decorators import method_decorator
from django.core.files.storage import default_storage

@method_decorator(csrf_exempt, name='dispatch')
class DecryptImage(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            encrypted_image_data = data.get('encryptedImage')
            if encrypted_image_data is None:
                return JsonResponse({'error': 'No encryptedImage field provided'}, status=400)

            # Decrypt the image using the decryption key (assuming it's known)
            encryption_key = 'VVBI8lKHuS8O+kavwbKMMLAa2zlh2kho'
            decrypted_image_data = decrypt_image(encrypted_image_data, encryption_key)

            # Convert the image to PNG format
            decrypted_image = Image.fromarray(np.frombuffer(decrypted_image_data, dtype=np.uint8)).convert('RGB')

            with default_storage.open('decrypted_image.png', 'wb') as f:
                decrypted_image.save(f, 'PNG')

            # Return the decrypted image as an HTTP response
            response = HttpResponse(decrypted_image, content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename="decrypted_image.png"'
            return response
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    def get(self, request):
        # Open the decrypted image file
        with default_storage.open('decrypted_image.png', 'rb') as f:
            image_data = f.read()

        # Return the decrypted image as an HTTP response
        response = HttpResponse(image_data, content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="decrypted_image.png"'
        return response