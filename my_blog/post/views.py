from django.http import HttpResponse
from django.shortcuts import render
from .models import Author,Entry

def update(request):
    author=Author.objects.get(id=1)
    author.name='Juanjo'
    author.email='juanjo@demo.com'
    author.save()
    return HttpResponse('Modificado')

def queries(request):
    #Obtener todos los elementos
    authors = Author.objects.all()
    #Obtener datos filtrando por condicion
    filtered = Author.objects.filter(email='morgan79@example.com')
    #Obtener un unico objeto
    author = Author.objects.get(id=1) 
    #Obtener los 10 primero  elementos
    limit = Author.objects.all()[:10]
    #Obtener 10 valores saltando los 5 primeros, puede ser en el filter tambien
    offset = Author.objects.all()[5:10]
    #Obtener todos los elementos ordenados
    orders = Author.objects.all().order_by('email')
    #Ontener todos los elementos cuyo id sea menor o igual a 15
    #__lte(menor o igual),__gte(mayor o igual),__lt(menor que),__gt(mayor que),__contains(contiene),__exact(exacto)
    filtereds = Author.objects.filter(id__lte=15)
    #Obtener tdos los autores que contienen la palabra yes
    filtereds2 = Author.objects.filter(name__contains='yes')

    return render(request,'post/queries.html',{'authors':authors,'filtered':filtered,'author':author,'limit':limit,'offset':offset,'orders':orders,'filtereds': filtereds,'filtereds2':filtereds2})
