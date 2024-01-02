from django.urls import path
from apps.base import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('gallery/', views.gallery, name='gallery'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('list/', views.list, name='list'),
    path('blog_detile/<int:id>/', views.post, name='post')
]
