from django.contrib import admin
from django.urls import path
from cosmosapp import views

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('list/', views.add_list, name="updated"),
]