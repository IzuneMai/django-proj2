from django.shortcuts import render

def profiles_home(request):
    return render(request, 'profiles/profiles_home.html')