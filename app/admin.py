from django.contrib import admin

# Register your models here.
from .models import MenuNames
from .models import MenuItems


class MenuNameAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'url', 'menu')


admin.site.register(MenuNames, MenuNameAdmin)
admin.site.register(MenuItems, MenuItemAdmin)
