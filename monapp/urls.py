from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_post_view, name='home'),
    path('post/new/', views.create_post_view, name='create_post'),
    path('post/<int:pk>', views.detail_post_view, name='detail_post'),
    path('post/<int:pk>/edit/', views.edit_post_view, name='edit_post'),
    path('post/<int:pk>/delete/', views.delete_post_view, name='delete_post'),
]