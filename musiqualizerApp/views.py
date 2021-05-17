"""App View Configuration"""

from django.shortcuts import render
from django.http import HttpResponse

# Homepage View
def homepage(request):
    return HttpResponse("First App")