from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),  #  login app
    path('foods/', include('foods.urls')),  #  foods app
]
