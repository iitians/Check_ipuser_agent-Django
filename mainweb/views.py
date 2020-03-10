from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .services import get_location
from .forms import get_car_data
from .models import CarDetail


class ListDisplay(LoginRequiredMixin, ListView):
    model = CarDetail
    template_name = 'mainweb/home.html'

    def get_context_data(self, **kwargs):
        context = super(ListDisplay, self).get_context_data(**kwargs)
        context['form'] = get_car_data
        return context

    def post(self, request, *args, **kwargs):
        form = get_car_data(request.POST)
        if form.is_valid():
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            form.instance.ip = ip
            user_agent = request.META.get('HTTP_USER_AGENT')
            form.instance.user_agent = user_agent
            location = get_location(ip)
            form.instance.location = location
            form.save()
            return redirect('home')
        form = get_car_data()
        return redirect('home')