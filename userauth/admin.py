from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import *

# Register your models here.

class UserAdmin(UserAdmin):
    list_display = ('email',)
    search_display = ('email', 'role')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)

admin.site.register(User, UserAdmin)