from django.urls import path, include
from . import views
from django.urls import path



urlpatterns = [
    
    path('',views.contact_view, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),

]