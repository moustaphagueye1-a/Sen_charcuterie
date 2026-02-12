from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:myid>/', views.detail, name='detail'),
    path('verifier/', views.verifier, name='verifier'),
]