from django.http import HttpResponse
from django.shortcuts import render
from .models import Reporter, Article
from datetime import date

def create(request):
    rep = Reporter(first_name='Juanjo',last_name='Ruiz', email='juanjo@demo.com')
    rep.save()

    art1 = Article(headline= 'Lorem ipsum dolot',pud_date=date(2023,5,5),reporter=rep)
    art1.save()
    art2 = Article(headline= 'Lorem set aimet',pud_date=date(2023,7,6),reporter=rep)
    art2.save()
    art3 = Article(headline= 'Lorem ipsum lorem',pud_date=date(2023,12,10),reporter=rep)
    art3.save()
    
    #Desde el reportero de uno a muchos
    #result = art1.reporter.first_name
    #Desde el Articulo de muchos a uno
    #result=rep.article_set.filter(headline= 'Lorem set aimet')
    result=rep.article_set.count()
    return HttpResponse(result)
