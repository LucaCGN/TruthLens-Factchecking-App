from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import auth

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
            # Verify the Firebase ID token
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            # Perform additional user checks or create a user session here

            return JsonResponse({'status': 'success', 'uid': uid})
        except auth.InvalidIdTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)
