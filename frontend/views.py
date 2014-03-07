from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from server.models import Category, Image


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        category = Category.objects.all().order_by('pozition')
        params = {
            'category': category,
        }
        return render(request, self.template_name, params)

    def post(self, request):

        return redirect("index")


class CategoryView(TemplateView):
    template_name = "category.html"

    def get(self, request, cat_id):
        category = Category.objects.all()
        images = Image.objects.filter(category_id = cat_id)
        params = {
            'category': category,
            'images': images,
        }

        return render(request, self.template_name, params)

    def post(self, request):
        return redirect("category")

# Create your views here.
