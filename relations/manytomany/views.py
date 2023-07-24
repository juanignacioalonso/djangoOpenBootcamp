from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Publication

def create(request):
    #Creacion de Articulos
    #art1=Article(headline="Articulo primero")
    #art1.save()
    #art2=Article(headline="Articulo segundo")
    #art2.save()
    #art3=Article(headline="Articulo tercero")
    #art3.save()

    #Creacion de Publicaciones
    #pub1=Publication(title="Publicacion primera")
    #pub1.save()
    #pub2=Publication(title="Publicacion segunda")
    #pub2.save()
    #pub3=Publication(title="Publicacion tercera")
    #pub3.save()
    #pub4=Publication(title="Publicacion cuarta")
    #pub4.save()
    #pub5=Publication(title="Publicacion quinta")
    #pub5.save()
    #pub6=Publication(title="Publicacion sexta")
    #pub6.save()
    #pub7=Publication(title="Publicacion sptima")
    #pub7.save()

    #Forma de relacionar los articulos con la publicaciones, primero deben estar guardados
    
    #art1.publications.add(pub1)
    #art1.publications.add(pub2)
    #art1.publications.add(pub3)
    #art2.publications.add(pub4)
    #art2.publications. 
    #art3.publications.add(pub7)
    
    #Para Borrar
    #art1.publications.remove(pub1)
    #Realizar una busqueda (SELECT)
    #result=art1.publications.all()
    #De forma inversa
    pub1 = Publication.objects.get(id=1)
    result= pub1.article_set.all()
    

    return HttpResponse(result)
