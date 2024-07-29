from django.urls import path, re_path
from apps.home import views
from django.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_subcategory/', views.add_subcategory, name='add_subcategory'),
     path('add_element/', views.add_element, name='add_element'),
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),
    path('data/', views.data, name='data'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_element/<int:element_id>/', views.edit_element, name='edit_element'),
    path('edit_element_value/', views.edit_element_value, name='edit_element_value'),
    path('change_status/<int:user_id>/', views.change_status, name='change_status'),
    re_path(r'^.*\.*', views.pages, name='pages'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)