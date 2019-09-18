from django.shortcuts import render
import smtplib


def landing_page(request):
    return render(request, 'Home/index.html')


def contact_form(request):
    name = request.POST.get('n')
    email = request.POST.get('e')
    subject = request.POST.get('sub')
    message = request.POST.get('msg')
    sender = 'mailautomationsdigital@gmail.com'
    receiver = sender
    print(name, email, subject, message)
    message += f"\n{name}\n{email}"
    message = 'Subject: {}\n\n{}'.format(subject, message)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    username = 'mailautomationsdigital@gmail.com'
    # change before deploying
    f = open('/home/aditya/PycharmProjects/AutomationsDigital/Home/passw.txt', 'r')
    password = f.read()
    server.login(username, password)
    server.sendmail(sender, receiver, message)
    server.quit()
    msg = "Successful"
    return render(request, 'Home/index.html', {'msg': msg})
