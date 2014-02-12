from django.contrib import admin
from models import Category, Image


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)


# Register your models here.
