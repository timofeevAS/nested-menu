from django import forms
from django.contrib import admin

from .models import MenuItem,Menu

class MenuItemAdmin(admin.ModelAdmin):
    # form = MenuItemForm
    list_display = ('name', 'menu', 'parent', 'url')
    list_filter = ('menu', 'parent',)
    prepopulated_fields = {'url': ('name',)}

    def save_model(self, request, obj, form, change):
        if obj.parent is None:
            print(obj.url)
            obj.url = ''
        else:
            obj.url = '/' + obj.menu.name + '/' + obj.url + '/'
        obj.save()




