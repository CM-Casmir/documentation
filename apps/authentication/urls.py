
from django.urls import path
from .views import login_view, logout_view, register_user, change_status,  delete_user
from apps.home.views import delete_element

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_user, name='register'),
    path('change_status/<int:user_id>/', change_status, name='change_status'),
    #  path('change_permissions/<int:user_id>/', change_permissions, name='change_permissions'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('delete_element/<int:element_id>/', delete_element, name='delete_element'),
]
