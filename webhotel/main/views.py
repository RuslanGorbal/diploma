from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def about_standart(request):
    return render(request, 'main/about_standart.html')


def about_deluxe(request):
    return render(request, 'main/about_deluxe.html')


def about_family(request):
    return render(request, 'main/about_family.html')


def about_luxe(request):
    return render(request, 'main/about_luxe.html')


def about_proluxe(request):
    return render(request, 'main/about_proluxe.html')


def about_business(request):
    return render(request, 'main/about_business.html')


def services(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/services.html', {'title': 'Послуги', 'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неправильна'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)