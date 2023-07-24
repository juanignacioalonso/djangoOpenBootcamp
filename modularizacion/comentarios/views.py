from django.http import HttpResponse
from django.shortcuts import render
from .models import Comment

def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
    #comment= Comment(name='Juanjo',score=5,comment='Este es un comenterio')
    #comment.save()
    comment = Comment.objects.create(name='Marcelo',score=6,comment='Este es el segundo comentario')
    return HttpResponse("Ruta crear")


def delete(request):
    #comment = Comment.objects.get(id=3)
    #comment.delete()
    Comment.objects.filter(id=4).delete()
    return HttpResponse("Ruta borrar")