# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from nerflix.models import Movie
from nerflix.forms import MovieForm 
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse



def movie_list(request):

    data = {}
    template_name = 'movie/movie_list.html'
    data['object_list'] = Movie.objects.all()
    return render(request, template_name, data)


def movie_create(request):
    template_name = 'movie/movie_form.html'
    form = MovieForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('movie_list'))
    return render(request, template_name, {'form': form})

def movie_update(request, pk):
    template_name = 'movie/movie_form.html'
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)

    if form.is_valid() :
        form.save()
        return HttpResponseRedirect(reverse('movie_list'))
    return render(request, template_name, {'form': form})

# def server_delete(request, pk, template_name='servers/server_confirm_delete.html'):
#     server = get_object_or_404(Movie, pk=pk)    
#     if request.method=='POST':
#         server.delete()
#         return redirect('server_list')
#     return render(request, template_name, {'object':server})