from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:token>', views.home, name='Home'),
    path('', views.make, name='Make New'),
]