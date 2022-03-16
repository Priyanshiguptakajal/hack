from django.contrib import admin
from .models import  Planets

admin.site.register(Planets)

# @admin.register(Planets)
# class UserAdmin(admin.ModelAdmin):
#     list_dispaly = ('name', 'distance', 'stars')

# Register your models here.
