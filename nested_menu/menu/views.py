
from django.shortcuts import render


def index(request, item=None):
    return render(request, 'index.html', {'item': item})