from django.urls import path
from . import views

# urls for home page
urlpatterns = [
    path('', views.index, name='home'),
    path('billabong/', views.billabong, name='billabong'),
    path('animal/', views.animal, name='animal'),
    path('oneill/', views.oneill, name='oneill'),
    path('gul/', views.gul, name='gul'),
]
