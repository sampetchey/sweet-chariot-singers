from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Vacancy
from .forms import VacancyForm
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


def save_vacancy(request):

    if request.method == "POST":
        # role = admin
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/team")
        
        else:
            form = VacancyForm()

        return render(request, "team.html", {"form": form}) 


def delete_vacancy(request, id):

    if request.method == "POST":
        obj = get_object_or_404(Vacancy, id = id)
        obj.delete()

        return HttpResponseRedirect("/team")


    return render(request, "team.html", {"form": form})


def update_vacancy(request, id):
    vacancy = Vacancy.objects.get(id=id)
    form = VacancyForm(request.POST, instance=vacancy)
    if form.is_valid():
        form.save()

        return HttpResponseRedirect("/team")
    
    else:
        form = VacancyForm()


    return render(request, "team.html", {"form": form})

# def update_vacancy(request, id):
#     vacancy = Vacancy.objects.get(id=id)

#     if request.method == "POST": 
#         form = VacancyForm(request.POST, instance=vacancy)
#         if form.is_valid():
#             form.save()

#             return HttpResponseRedirect("/team")
        
#         else:
#             form = VacancyForm(instance=vacancy)

#         return render(request, "team.html", {"form": form}) 