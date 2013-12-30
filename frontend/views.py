from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        params = {}
        return render(request, self.template_name, params)

    def post(self, request):
        return redirect("index")


# Create your views here.