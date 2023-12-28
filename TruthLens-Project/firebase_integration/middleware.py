from firebase_admin import auth, exceptions
from django.contrib.auth.models import User
from django.http import JsonResponse

class FirebaseAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the ID token from the Authorization header
        id_token = request.headers.get('Authorization')
        if id_token:
            try:
                # Remove 'Bearer ' prefix to get the actual token
                id_token = id_token.split('Bearer ')[1]
                # Verify the token
                decoded_token = auth.verify_id_token(id_token)
                # Get or create a user from the decoded token
                uid = decoded_token['uid']
                user, created = User.objects.get_or_create(username=uid)
                # Attach the user to the current request
                request.user = user
            except auth.InvalidIdTokenError:
                # Token is invalid
                return JsonResponse({'error': 'Invalid token'}, status=401)
            except ValueError:
                # Token is malformatted
                return JsonResponse({'error': 'Malformatted token'}, status=401)
            except exceptions.FirebaseError:
                # Firebase error
                return JsonResponse({'error': 'Firebase error'}, status=401)
        else:
            # No token provided
            request.user = None

        # Call the next middleware in the chain
        response = self.get_response(request)
        return response
