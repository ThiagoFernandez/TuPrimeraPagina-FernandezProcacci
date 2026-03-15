from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Page


def inicio(request):

    return render(request, "blog/inicio.html")


def about(request):

    return render(request, "blog/about.html")


class PageList(ListView):

    model = Page

    template_name = "blog/pages.html"


class PageDetail(DetailView):

    model = Page

    template_name = "blog/page_detail.html"


class PageCreate(LoginRequiredMixin, CreateView):

    model = Page

    fields = '__all__'

    template_name = "blog/form.html"

    success_url = reverse_lazy('pages')


class PageUpdate(LoginRequiredMixin, UpdateView):

    model = Page

    fields = '__all__'

    template_name = "blog/form.html"

    success_url = reverse_lazy('pages')


class PageDelete(LoginRequiredMixin, DeleteView):

    model = Page

    template_name = "blog/delete.html"

    success_url = reverse_lazy('pages')