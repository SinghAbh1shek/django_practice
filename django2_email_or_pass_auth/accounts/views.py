from django.shortcuts import render, redirect
from custom_auth.models import CustomUser
from django.contrib.auth import login
from django.db import IntegrityError

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_phone = request.POST.get('email_phone').replace(" ", "")  # replace for removing whitespace
        password = request.POST.get('password')
        passwordConfirmation = request.POST.get('passwordConfirmation')

        if not email_phone or not password or not passwordConfirmation:
            print({'error': 'all fields are required'})
            return redirect('register.html')
        
        if password != passwordConfirmation:
            print({'error': 'passwords do not match'})
            return redirect('register')
        
        if '@' in email_phone:
            is_email = True
        elif email_phone.isdigit() and len(email_phone) == 10:
            is_email = False
        else:
            print({'error': 'Enter a valid email or password'})
            return redirect('register')
        
        if is_email:
            if CustomUser.objects.filter(email = email_phone).exists():
                print({'error': 'Email already exist'})
                return redirect('register')
        else:
            if CustomUser.objects.filter(phone_number = email_phone).exists():
                print({'error': 'Phone number already exist'})
                return redirect('register')
            
        try:
            if is_email:
                user = CustomUser.objects.create_user(
                    username = email_phone,
                    first_name = first_name,
                    last_name = last_name,
                    email= email_phone,
                    password=password
                )
            else:
                user = CustomUser.objects.create_user(
                    username = email_phone,
                    first_name = first_name,
                    last_name = last_name,
                    phone_number = email_phone,
                    password=password
                )
            login(request, user)
            return redirect('home')
        
        except IntegrityError:
            print('Phone Number or email already exist')
            return redirect('register')

        except ValueError as e:
            print(e)
            return redirect('register')
        
        except:
            print('Something went Wrong')
            return redirect('register')
        
    return render(request, 'register.html')
