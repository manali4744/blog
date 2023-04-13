from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('id', 'name', 'is_admin', 'is_valid')
    # inlines = [CardDetailInline]
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('password',)}),
        ('Personal info', {'fields': ('name','email','is_valid',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ['name', 'password1', 'password2',],
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.register(Blogger)
