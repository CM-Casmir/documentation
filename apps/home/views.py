
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect,  JsonResponse
from django.template import loader, TemplateDoesNotExist
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Subcategory, Element, Data
from .forms import CategoryForm, SubcategoryForm, ElementForm, DataForm
from django.contrib import messages
from django.utils import timezone
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.contrib.auth.models import User
from django.db import IntegrityError 


@login_required(login_url="/auth/login/")
def index(request):
    return redirect('dashboard')

@login_required(login_url="/auth/login/")
def pages(request):
    context = {}

    try:
        load_template = request.path.split('/')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/auth/login/")
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
            return redirect('add_category')
        else:
            messages.error(request, 'Form validation failed. Please check the inputs.')
    else:
        form = CategoryForm()
    return render(request, 'home/add_category.html', {'form': form})

@login_required(login_url="/auth/login/")
def add_subcategory(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subcategory added successfully.')
            return redirect('add_subcategory')
        else:
            messages.error(request, 'Form validation failed. Please check the inputs.')
    else:
        form = SubcategoryForm()
    
    categories = Category.objects.all()
    return render(request, 'home/add_subcategory.html', {'form': form, 'categories': categories})

@login_required(login_url="/auth/login/")
def add_element(request):
    if request.method == "POST":
        form = ElementForm(request.POST)
        if form.is_valid():
            element = form.save()
            category = element.category
            subcategory = element.subcategory

            if subcategory:
                messages.success(request, f'Element "{element.title}" added successfully in subcategory "{subcategory.name}".')
            else:
                messages.success(request, f'Element "{element.title}" added successfully in category "{category.name}".')
            
            return redirect('add_element')
    else:
        form = ElementForm()

    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return render(request, 'home/add_element.html', {
        'form': form,
        'categories': categories,
        'subcategories': subcategories,
    })

def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id)
    subcategories_list = [{'id': subcategory.id, 'name': subcategory.name} for subcategory in subcategories]
    return JsonResponse(subcategories_list, safe=False)

@login_required(login_url="/auth/login/")
def data(request):
    if request.method == 'POST':
        element_id = request.POST.get('element')
        element = get_object_or_404(Element, id=element_id)
        value = request.FILES.get('value') if element.element_type in ['image', 'pdf'] else request.POST.get('value')

        # Save the data
        Data.objects.create(element=element, value=value)
        messages.success(request, 'Data added successfully.')

        return redirect('data')  # Redirect to the same page to clear the form

    subcategory_id = request.GET.get('subcategory')
    elements = Element.objects.filter(subcategory_id=subcategory_id) if subcategory_id else Element.objects.none()
    selected_element_id = request.GET.get('element')
    selected_element = get_object_or_404(Element, id=selected_element_id) if selected_element_id else None

    return render(request, 'home/data.html', {
        'subcategories': Subcategory.objects.all(),
        'elements': elements,
        'selected_element': selected_element,
    })


@login_required(login_url="/auth/login/")
def dashboard(request):
    categories = Category.objects.all()
    users = User.objects.all()

    selected_element = None
    data = None
    if 'element' in request.GET:
        selected_element = get_object_or_404(Element, id=request.GET['element'])
        data = selected_element.data.first()  # Fetch the first data instance

    return render(request, 'home/dashboard.html', {
        'categories': categories,
        'users': users,
        'selected_element': selected_element,
        'data': data
    })

@login_required(login_url="/auth/login/")
def edit_element(request, element_id):
    element = get_object_or_404(Element, id=element_id)
    try:
        data_instance = Data.objects.get(element=element)
    except Data.DoesNotExist:
        data_instance = None

    if request.method == 'POST':
        form = DataForm(request.POST, instance=data_instance)
        if form.is_valid():
            form.instance.element = element
            form.save()
            messages.success(request, 'Element updated successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Form validation failed. Please check the inputs.')
    else:
        form = DataForm(instance=data_instance)
    return render(request, 'home/edit_element.html', {'form': form, 'element': element})

@login_required(login_url="/auth/login/")
def edit_element_value(request):
    if request.method == 'POST':
        element_id = request.POST.get('element_id')
        value = request.POST.get('value')

        if not value and not request.FILES:
            messages.error(request, 'Value cannot be empty.')
            return redirect('dashboard')

        element = get_object_or_404(Element, id=element_id)
        data, created = Data.objects.get_or_create(element=element)

        if element.element_type in ['image', 'pdf']:
            value = request.FILES.get('value')

        data.value = value
        data.save()

        messages.success(request, 'Element value updated successfully.')
        return redirect('dashboard')

    return render(request, 'dashboard.html')

    return render(request, 'dashboard.html')  # Render the dashboard if the request method is not POST
@login_required
def delete_element(request, element_id):
    element = get_object_or_404(Element, id=element_id)
    element.delete()
    messages.success(request, 'Element deleted successfully.')
    return redirect('dashboard')

@login_required
def change_status(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = not user.is_active
    user.save()
    messages.success(request, f'User status changed to {"Active" if user.is_active else "Inactive"}.')
    return redirect('dashboard')

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('dashboard')
