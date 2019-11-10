from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def index(request):
    """
       Public interface to the flat page view.
       Templates:
       Context:
           flatpage
               `flatpages.flatpages` object
    """
    context = {}

    return render(request, 'main/main.html', context)

