from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dev_team_website_app/home.html')

def projects(request):
    return render(request, 'dev_team_website_app/projects.html')