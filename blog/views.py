from django.shortcuts import render
from django.http  import Http404, HttpResponse
import sys
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import BlogUser
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    return render(request, "AuthTemplate/register.html")

def login(request):
    return render(request, "AuthTemplate/login.html")

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
    elif request_type == 'login' and request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            user = BlogUser.objects.get(email = email)
            
            if(check_password(password, user.password)):
                 return JsonResponse({'status': 200, 'message': 'User login successful'})
            else:
                 raise ValidationError("Invalid email or password")
        except BlogUser.DoesNotExist:
            raise ValidationError("Invalid email or password")
        except ValidationError as e:
            return JsonResponse({'status': 400, 'message': str(e.message)})
        except Exception as e:
            return JsonResponse({'status': 500, 'message': str(e)})
    else:
        raise Http404('Page not found')
    
    
    
# admin dashboard
@login_required(login_url='/blog/login')
def admin_dashboard(request):
    return HttpResponse('Hare Krishna and Hare Rama')

            
            
            
            
        # return JsonResponse({'status':403, 'message':'Invalid request'})