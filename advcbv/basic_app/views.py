from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models
# Create your views here.

class SchoolList(ListView):
    context_object_name='schools'
    model = models.School

class SchoolDetail(DetailView):
    context_object_name='school_detail'
    model=models.School
    template_name='basic_app/School_detail.html'


#Below code is for Class Based Views
class CBView(View):
    def get(self,request):
        return HttpResponse("This is sample Page")

class Index(TemplateView):
    template_name="index.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme'] = 'THIS IS A SAMPLE INJCTION from GITHUB'
        return context
