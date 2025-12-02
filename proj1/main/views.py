from django.shortcuts import render


def index(request):
    data ={
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)


def profile(request):
    return render(request, 'main/profile.html')

def guides(request):
    return render(request, 'main/guides.html')