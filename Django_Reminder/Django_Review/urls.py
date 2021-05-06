from django.conf.urls import url, include
from Django_Review import views
from django.urls import path


urlpatterns =[
    path('',views.home, name='home'),
    path('inventory',views.weapons_inv, name='inventory'),
    path('add_weapon', views.add_weapon, name="add_weapon"),
]