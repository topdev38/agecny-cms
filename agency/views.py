from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings

from .models import Subscriber, Contact, Team_member, Customer


def home(request):
    context = {
        "page": 'home',
    }
    return render(request, "home.html", context)

def subscribe(request):
    if request.method == 'POST':
        if Subscriber.objects.filter(email=request.POST['email']):
            return HttpResponse('exist')
        else:
            subscribe = Subscriber(email=request.POST['email'])
            subscribe.save()
            return HttpResponse('Success')
    return HttpResponse('Failed')

def contact(request):
    if request.method == 'POST':
        contact = Contact(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            text = request.POST['message']
        )
        contact.save()
        try:
            email_subject = 'New contact info'
            message = "First name: {}<br> Last name: {}<br> Email address: {}<br> Phone number: {}<br> Text: {}<br>".format(
                request.POST['first_name'],
                request.POST['last_name'],
                request.POST['email'],
                request.POST['phone'],
                request.POST['message']
            )
            to_email = 'paulkatok77@gmail.com'
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
        except Exception as e:
            print(e)
        return HttpResponse('Success')
    return HttpResponse('Failed')

def about(request):
    context = {
        "page": "about",
    }
    return render(request, "about.html", context)

def services(request):
    context = {
        "page": "services",
    }
    return render(request, "services.html", context)

def projects(request):
    context = {
        "page": "projects",
    }
    return render(request, "projects.html", context)

def projects_detail(request):
    context = {
        "page": "projects_detail",
    }
    return render(request, "projects_detail.html", context)

def contact_us(request):
    context = {
        "page": "contact_us",
    }
    return render(request, "contact_us.html", context)

def blog(request):
    context = {
        "page": "blog",
    }
    return render(request, "blog.html", context)

def blog_detail(request):
    context = {
        "page": "blog_detail",
    }
    return render(request, "blog_detail.html", context)