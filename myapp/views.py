from django.shortcuts import render
from django.http import HttpResponse

import myapp.views


def index(request):
    data = {
        'title': 'main sheet',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'myapp/index.html', data)
def about(request):
    return render(request, 'myapp/about.html')
def contact(request):
    return render(request, 'myapp/contact.html')
