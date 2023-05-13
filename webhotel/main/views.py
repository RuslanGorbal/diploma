from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
import openai, os
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("OPENAI_KEY", None)


def chatbot(request):
    chatbot_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = f"Якщо питання відвідувача буде відноситись до сфери готелю то, " \
                 f"уяви, що ти онлайн-консультант готелю Карпати, для початку привітайся з відвідувачем, " \
                 f"а потім дай відповідь на його питання: {user_input}"

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            temperature=0.5
        )
        print(response)

        chatbot_response = response["choices"][0]["text"]
    return render(request, 'main/qa.html', {"response": chatbot_response})


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
    return render(request, 'main/services.html')


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


def create_receipt(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/create_receipt.html', {'title': 'Чек', 'tasks': tasks})