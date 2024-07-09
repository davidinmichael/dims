from django.contrib.auth import login, authenticate, get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Dataset  # Import your Dataset model
import json

User = get_user_model()

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        # Validate username and password
        if not username or not password:
            return JsonResponse({'error': 'Username and password are required'}, status=400)
        
        # Create new user
        try:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)  # Log the user in after registration
            return JsonResponse({'message': 'User registered successfully'})
        except Exception as e:
            return JsonResponse({'error': f'Failed to register user: {str(e)}'}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        # Validate username and password
        if not username or not password:
            return JsonResponse({'error': 'Username and password are required'}, status=400)
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def profile(request):
    if request.user.is_authenticated:
        datasets = Dataset.objects.filter(user=request.user)
        dataset_list = list(datasets.values())  # Convert QuerySet to list of dictionaries
        return JsonResponse({'datasets': dataset_list})
    
    return JsonResponse({'error': 'Unauthorized'}, status=401)