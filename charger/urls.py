from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('map/', views.map_view, name='map_page'),
    path('charging/', views.charging_view, name='charging'),
    path('about/', views.about, name='about'),
    path('calculate/', views.calculate_charge, name='calculate_charge'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/set-charging/', views.set_charging_state, name='set-charging'),
    path('api/charger-data/', views.get_charger_data, name='charger-data'),
]