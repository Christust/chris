from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Entry

# Create your views here.
def queries(request):
    # Obtener todos los elementos
    authors = Author.objects.all()

    # Obtener datos filtrados
    filtered = Author.objects.filter(email="bryantjeffrey@example.org")
    
    # Obtener un unico objeto
    author = Author.objects.get(id=1)

    #Obtener los primeros 10 elementos
    limited = Author.objects.all()[:10]

    return render(request, 'queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limited': limited } )