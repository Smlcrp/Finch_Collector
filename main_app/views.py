from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from .models import Duck



# Create your views here.

class Home(TemplateView):
   template_name = 'home.html'


class DuckList(TemplateView):
    template_name = 'duck_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['ducks'] = Duck.objects.filter(name__icontains=name)
            context['header'] = f"Searching For {name}"
        else:
            context['ducks'] = Duck.objects.all()
            context['header'] = "All The Ducks"
        return context



class DuckCreate(CreateView):
    model = Duck
    fields = ['name', 'img', 'bio']
    template_name = 'duck_create.html'
    def get_success_url(self):
        return reverse('duck_detail', kwargs={'pk': self.object.pk})


class DuckDetail(DetailView):
    model = Duck
    template_name = 'duck_detail.html'


class DuckUpdate(UpdateView):
    model = Duck
    fields = ['name', 'img', 'bio']
    template_name = 'duck_update.html'
    def get_success_url(self):
        return reverse('duck_detail', kwargs={'pk': self.object.pk})


class DuckDelete(DeleteView):
    model = Duck
    template_name = 'duck_delete_confirmation.html'
    success_url = '/ducks/'