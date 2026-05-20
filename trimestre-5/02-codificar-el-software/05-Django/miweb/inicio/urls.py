from django.urls import path
from . import views

urlpatterns = [
    # Aqui ya hablamos del futuro porque tendremos una función llamada home
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contacto/', views.contacto, name='contacto')
]