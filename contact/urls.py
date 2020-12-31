from django.urls import path
from . import views

# urls for contact page
urlpatterns = [
    path('', views.contact, name='contact'),
]
