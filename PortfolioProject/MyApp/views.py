from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.conf import settings as django_settings
from . import models
from . import utility

# Create your views here.

def home(request):
    try: #if home table exists
        home = models.Home.objects.get(id = models.Home.objects.all().values("id").last()["id"]) #get the last id created
    except:
        home = None
    try:
        about = models.About.objects.get(id = models.About.objects.all().values("id").last()["id"])
    except:
        about = None
    try:
        resumes = models.Resume.objects.get(id = models.Resume.objects.all().values("id").last()["id"])
    except:
        resumes = None
    try:
        portfolio_group = models.PortfolioGroup.objects.filter()
        portfolios = models.MyPortfolio.objects.filter()
    except:
        portfolio_group = None
        portfolios = None
    try:
        services = models.Service.objects.get(id = models.Service.objects.all().values("id").last()["id"])
    except:
        services = None
    try:
        testimonies = models.Testimonial.objects.all()
    except:
        testimonies = None
    try:
        contact = models.Contact.objects.get(id = models.Contact.objects.all().values("id").last()["id"])
    except:
        contact = None
    try:
        settings = models.Setting.objects.get(id=models.Setting.objects.all().values("id").last()["id"])
    except:
        settings = None

    context = {
        "home" : home,
        "about" : about,
        "resumes" : resumes,
        "portfolios" : portfolios,
        "portfolio_group" : portfolio_group,
        "services" : services,
        "testimonies" : testimonies,
        "contact" : contact,
        "settings" : settings
        
    }

    return render(request, "MyApp/index.html", context)


def contactForm(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        msg = request.POST.get("message")
        #send an email to me
        try:
            utility.emailSender(name, django_settings.EMAIL_HOST_USER, [email], msg, subject)
            return redirect("contact")
        except:
            messages.error(request, "Message wasn't sent.Please Try again")
    return redirect("home")