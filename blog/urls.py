from django.urls import path, include
from . import views
from django.urls import path



urlpatterns = [
     path('', views.PostList.as_view(), name='home'),
     path('search/',views.searchpost, name ='search'),
     path('<slug:slug>/', views.post_detail, name='post_detail'),
     path('<slug:slug>/create_post', views.create_post, name='create_post'),
     path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
     path('<slug:slug>/update/', views.PostUpdateView.as_view(), name='update_post'),
     path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
     path('like/<slug:slug>', views.post_like, name='post_like'),
     ]
