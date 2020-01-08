from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import *
# from .models import About
# from .models import Skills
# from .models import Projects

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        # context['details'] = Details.objects.all()
        context['skills'] = Skills.objects.all()
        context['projects'] = Projects.objects.all()
        return context

# def home(request):
#     return HttpResponse('<h1>home pageesd</h1>')

def about(request):
    return HttpResponse('<h1>about pageee</h1>')

def projects(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)
