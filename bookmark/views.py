from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from bookmark.models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark
    #bookmark_list.html, {'bookmark_list': Bookmark.objects.all()}
    #render(request, 'bookmark_list.html', {'bookmark_list': Bookmark.objects.all()})

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name', 'url']           #'__all__'
    template_name_suffix = '_create'    #bookmark_from.html -> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['name', 'url']    #'__all__'
    template_name_suffix = '_update'    #bookmark_Update.html
    success_url = reverse_lazy('bookmark:list') #success_url이 없으면 model의 get_absolute_url() 호출