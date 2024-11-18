from django.shortcuts import render
from .models import Services, Posts, Team, Users


# Create your views here.


def home(request):
    posts = Posts.objects.all()
    return render(request, 'index.html', {'posts': posts})


def about(request):
    teams = Team.objects.all()
    return render(request, 'about.html', {'team': teams} )

def services(request):
    services = Services.objects.all()
    return render(request, 'services.html', {'services': services})


def contact(request):
    return render(request, 'contact.html')


def insert_data(request):
   if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        user = Users(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        user.save()




   return render(request, 'contact.html')





