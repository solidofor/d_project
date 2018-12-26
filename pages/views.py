from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html',context)

def about(request):
    realtors = Realtor.objects.order_by('-id')[:3]
    mvp_realtors = Realtor.objects.order_by('-id').filter(is_mvp=True)[:1]
    context = {
        'realtors': realtors,
        'mvp_realtors' : mvp_realtors
    }
    return render(request, 'pages/about.html',context)