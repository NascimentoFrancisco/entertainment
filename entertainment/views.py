from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
        CreateView, ListView,UpdateView, DeleteView,
        DetailView
    )

from .models import Entertainment
# Create your views here.

class CreateEntertainment(LoginRequiredMixin, CreateView):

    model = Entertainment
    login_url = reverse_lazy('accounts:login_user')
    template_name = 'create.html'
    fields = ['title','type','review']
    success_url = reverse_lazy('entertainment:home_entertainment')

    def form_valid(self, form):
        
        form.instance.user = self.request.user
        form.instance.end_date = timezone.now()
        title = form.data['title']

        messages.success(self.request, 
            f'{title} criado com sucesso!'
        )
        return super().form_valid(form)

class ListEntertainment(LoginRequiredMixin, ListView):
    
    template_name = 'entertainment/list.html'
    login_url = reverse_lazy('accounts:login_user')

    def get_queryset(self):
        queryset = Entertainment.objects.filter(user = self.request.user)
        return queryset


class UpdateEntertainment(LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy('accounts:login_user')
    model = Entertainment
    template_name = 'create.html'
    fields = ['title','type','status','review']
    success_url = reverse_lazy('entertainment:home_entertainment')

    def form_valid(self, form):
        
        messages.success(self.request, 
            f'{self.get_object().title} alterado com sucesso!'
        )
        return super().form_valid(form)

class FinishEntertainment(LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy('accounts:login_user')
    model = Entertainment
    template_name = 'entertainment/finish.html'
    fields = []
    success_url = reverse_lazy('entertainment:home_entertainment')

    def form_valid(self, form):

        form.instance.status = True
        form.instance.end_date = timezone.now()
            
        messages.success(self.request, 
            f'{self.get_object().title} finalização com sucesso!'
        )
        return super().form_valid(form)

class DetailEntertainment(LoginRequiredMixin, DetailView):

    model = Entertainment
    login_url = reverse_lazy('accounts:login_user')
    template_name = 'entertainment/detail.html'

class DeleteEntertainment(LoginRequiredMixin, DeleteView):

    model = Entertainment
    login_url = reverse_lazy('accounts:login_user')
    template_name = 'entertainment/delete.html'
    success_url = reverse_lazy('entertainment:home_entertainment')

    def get_success_url(self):
        
        messages.success(self.request,
            f'{self.get_object().title} apagado com sucesso!'
        )
        return super().get_success_url()
