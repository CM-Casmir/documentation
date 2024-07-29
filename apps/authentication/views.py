from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Profile
from django.db import IntegrityError
from django.contrib.auth.decorators import  login_required
from django.urls import reverse
from apps.home.models import Element, Category
from django.contrib.contenttypes.models import ContentType

def login_view(request):
    form = CustomAuthenticationForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    msg = 'This account is inactive.'
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
    return render(request, 'accounts/login.html', {'form': form, 'msg': msg})

def register_user(request):
    msg = None
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                fullname = form.cleaned_data.get('fullname')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')

                user = User.objects.create_user(username=email, email=email, password=password)
                user.first_name = fullname
                user.save()

                Profile.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))

                messages.success(request, 'Account created successfully. Please log in.')
                return redirect('login')  
            except IntegrityError:
                msg = 'Account created successfully. Please log in.'
        else:
            msg = 'Form is not valid'
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form, 'msg': msg})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html', {
        'users': User.objects.all(),
        'categories': Category.objects.prefetch_related('subcategories__elements__data').all()
    })

# @login_required
# def dashboard_read_only(request):
#     return render(request, 'home/dashboard_read_only.html', {
#         'categories': Category.objects.prefetch_related('subcategories__elements__data').all()
#     })


# Change user status view
@login_required
def change_status(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = not user.is_active
    user.save()
    return redirect('dashboard')

# Change user permissions view
# @permission_required('auth.change_user', raise_exception=True)
# def change_permissions(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     profile = user.profile

#     if profile.permission == 'read_write':
#         profile.permission = 'read_only'
#     else:
#         profile.permission = 'read_write'
#     profile.save()
#     return redirect('dashboard')

# Delete user view
@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('dashboard')

# Delete element view
@login_required
def delete_element(request, element_id):
    element = get_object_or_404(Element, id=element_id)
    element.delete()
    return redirect('dashboard')