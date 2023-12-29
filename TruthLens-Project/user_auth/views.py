from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import auth
from .models import CustomUser
from firebase_integration.firestore_client import create_user_document

def sign_in(request):
    """
    Render the sign-in page.
    """
    return render(request, 'user_auth/sign_in.html')

@csrf_exempt
def verify_token(request):
    """
    Verify the Firebase token and authenticate the user.
    """
    if request.method == 'POST':
        token = request.POST.get('token')
        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            
            # Create or update user in Django's auth system
            user, created = CustomUser.objects.get_or_create(firebase_uid=uid)

            # Create a new document in Firestore for the user
            if created:
                create_user_document(uid)

            return JsonResponse({'status': 'success', 'uid': uid})
        except auth.InvalidIdTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)
