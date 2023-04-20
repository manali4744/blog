from django.contrib import admin
from .models import *
# Register your models here.

# class WriteblogAdmin(admin.ModelAdmin):
#     model = Write
#     list_display = ['blog_writer', 'title']



admin.site.register(BlogWrite)
admin.site.register(Writer)
