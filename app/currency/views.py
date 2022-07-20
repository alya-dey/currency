from django.http import HttpResponse  # noqa
from django.shortcuts import render
from currency.models import ContactUs, Rate


def index(request):
    return render(request, 'index.html')


def contacts_responses(request):
    context = {
        'contact_us_list': ContactUs.objects.all(),
    }

    return render(request, 'contact_us.html', context=context)


def rate_list(request):
    context = {
        'rate_list': Rate.objects.all(),
    }

    return render(request, 'rate_list.html', context=context)
