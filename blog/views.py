from django.shortcuts import render
from django.http import HttpResponse
import sys
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import BlogUser
from django.core.exceptions import ValidationError
# Create your views here.
def register(request):
    return render(request, "AuthTemplate/register.html")

# save user
def SaveUser(request, request_type):
    if request.method == 'POST' and request_type=='add':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = make_password(request.POST.get('password'))
            
            if(not(BlogUser.objects.filter(email=request.POST.get('email'))).exists()):
                BlogUser.objects.create(name=name, email=email, password=password)
                return JsonResponse({'status':201, 'message':'User created successfully'})
            raise ValidationError("Email already exists")
        except ValidationError as e:
            return JsonResponse({'status': 400, 'message': str(e.message)})
        except Exception as e:
            return JsonResponse({'status':500, 'message':str(e)})
    else:
        return JsonResponse({'status':403, 'message':'Invalid request'})