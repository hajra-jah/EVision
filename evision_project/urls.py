from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('charger.urls')), # Ye line app ke saare urls connect kar degi
]