from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from . models import ContactForm

def emailView(request):
    if request.method == 'GET':
        models = ContactForm()
    else:
        models = ContactForm(request.POST)
        if models.is_valid():
            subject = models.cleaned_data['subject']
            from_email = models.cleaned_data['from_email']
            message = models.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@dineshganapathi.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request,  'personal/basic.html', {'models': modles})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
