from django.contrib import admin
from models import Category, Image


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class ImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Image, ImageAdmin)

# Register your models here.
