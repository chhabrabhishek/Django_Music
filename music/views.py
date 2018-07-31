from django.http import HttpResponse,Http404
from .models import Album
from django.shortcuts import render,get_object_or_404
from django.template import loader

def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    #return HttpResponse(template.render(context,request))
    return render(request,'music/index.html',{'all_albums':all_albums})

def details(request,album_id):
    #try:
    #    album = Album.objects.get(pk = album_id)
    #except:
    #   raise Http404("Album does not exist")
    album = get_object_or_404(Album,pk=album_id)
    return render(request,'music/details.html',{'album':album})