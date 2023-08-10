from django.shortcuts import render
from .models import Vacancy

# Create your views here.

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def visit(request):
    return render(request, 'home/visit.html')

def team(request):
    vacancies = Vacancy.objects.all()
    context = {
        'vacancies': vacancies
    }
    
    return render(request, 'home/team.html', context)