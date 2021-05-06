from django.conf.urls import url, include
from Django_Review import views
from django.urls import path


urlpatterns =[
    path('',views.home, name='home'),
    path('inventory',views.weapons_inv, name='inventory'),
    path('add_weapon', views.add_weapon, name="add_weapon"),
    path('delete_weapon/<int:pk>/', views.delete_weapon, name="delete_weapon"),
    path('edit_weapon/<int:pk>/', views.edit_weapon, name="edit_weapon"),
    path('confirm_order', views.confirm_order, name="confirm_order"),
]