from django.shortcuts import render
from apps.base.models import Settings, Servise, About
# Create your views here.
def index(request):
    servise = Servise.objects.all()
    settings = Settings.objects.latest("id")
    about = About.objects.latest("id")
    return render(request, 'index.html', locals())  

def blog_list(request):
    return render(request, 'blog_list.html', locals() )

def blog_details(request):
    return render(request, 'blog_details.html', locals() )
