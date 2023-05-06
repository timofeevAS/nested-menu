from django.contrib import admin
from menu.models import MenuItem, Menu


class MenuItemAdmin(admin.ModelAdmin):
    # form = MenuItemForm
    list_display = ('name', 'menu', 'parent', 'url')

    def save_model(self, request, obj, form, change):
        obj.url = '/' + obj.menu.name + '/' + obj.url + '/'
        obj.save()


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu)