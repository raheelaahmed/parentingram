from . import views
from django.urls import path

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit_profile<int:pk>/', views.EditProfileView.as_view(), name='edit_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile')
]