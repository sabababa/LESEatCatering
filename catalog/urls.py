from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('services/', views.services, name='services'),
    path('menus/', views.menus, name='menus'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('confirm/', views.confirm, name='confirm'),
]
