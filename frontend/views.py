from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from server.models import Category


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        category = Category.objects.all().order_by('pozition')
        params = {
            'category': category,
            'background': 'img/background.jpg',
        }
        return render(request, self.template_name, params)

    def post(self, request):

        return redirect("index")


# Create your views here.
