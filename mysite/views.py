from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext


def home(request):
    return redirect('index')
