from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Example URL pattern
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
      # Another example
]
