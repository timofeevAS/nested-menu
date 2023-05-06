from django.contrib import admin
from menu.models import MenuItem, Menu
from menu.forms import MenuItemAdmin


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu)