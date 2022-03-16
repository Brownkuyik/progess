from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from mainwork.models import company, slight, AboutDetails, whyus, whypoint, serviceDetail, testimonial, team, QandA

def home(request):
    return render(request, 'index1.html')


def sol(request):
    return render(request, 'index23.html')

def post(request):
    hall = company.objects.all()
    frot = slight.objects.all()
    why = whyus.objects.all()
    so = whypoint.objects.all()
    about = AboutDetails.objects.all()
    service = serviceDetail.objects.all()
    test = testimonial.objects.all()
    terms = team.objects.all()
    ask = QandA.objects.all()
    there = {
        'company': hall,
        'slight': frot,
        'about': about,
        'why': why,
        'waoo': so,
        'save': service,
        'tes': test,
        'term': terms,
        'what': ask

    }
    return render(request, 'home.html', there)

def main(request):
    hall = company.objects.all()
    frot = slight.objects.all()
    why = whyus.objects.all()
    so = whypoint.objects.all()
    about = AboutDetails.objects.all()
    service = serviceDetail.objects.all()
    test = testimonial.objects.all()
    terms = team.objects.all()
    ask = QandA.objects.all()
    there = {
        'company': hall,
        'slight': frot,
        'about': about,
        'why': why,
        'waoo':so,
        'save':service,
        'tes':test,
        'term':terms,
        'what':ask

    }
    return render(request, 'where/home.html', there)


