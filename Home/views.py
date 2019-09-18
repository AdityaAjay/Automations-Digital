from django.shortcuts import render
import smtplib


def landing_page(request):
    return render(request, 'Home/index.html')


def contact_form(request):
    name = request.POST.get('Name')
    email = request.POST.get('Email')
    subject = request.POST.get('Subject')
    message = request.POST.get('Message')
    pass
