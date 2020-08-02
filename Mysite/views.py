from django.shortcuts import render
from .models import Contact
import requests, json


def index(request):
    if request.method == "POST":
        finame = request.POST.get('fname')
        laname = request.POST.get('lname')

        r = requests.get('https://favqs.com/api/qotd')
        json_data = json.loads(r.text)
        quote = json_data.get('quote').get('body')
        context = {'quoter': quote, 'finame': finame, 'laname': laname}

        return render(request, 'Mysite/index.html', context)
    else:
        return render(request, 'Mysite/index.html')


def portfolio(request):
    return render(request, 'Mysite/portfolio.html')


def contact(request):
    if request.method == 'POST':
        email_store = request.POST.get('email')
        subject_store = request.POST.get('subject')
        message_store = request.POST.get('message')

        c = Contact(email=email_store, subject=subject_store, message=message_store)

        c.save()
        return render(request, 'Mysite/thanku.html')
    else:
        return render(request, 'Mysite/contact.html')
