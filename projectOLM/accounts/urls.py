from django.urls import path

from . import views

urlpatterns = [

    path('register', views.register, name = 'request'),
    path('logout', views.logoutU, name = 'logoutU'),
    path('getEduPlace',views.getEduPlace, name = 'getEduPlace')
]