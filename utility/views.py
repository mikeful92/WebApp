__author__ = 'Mike'

from django.http import HttpResponseRedirect, request, HttpResponse
from django.shortcuts import render, get_list_or_404
from django.core.urlresolvers import reverse

from utility.models import ElectricConsumption

def index(request):
    return render(request, 'utility/index.html')

def lookup(request):
    return render(request, 'utility/lookup.html')

def backend(request):
    address = request.POST['address']
    my_object = get_list_or_404(ElectricConsumption, service_address=address)
    context = {'address': address,
               'my_object': my_object}
    return render(request, 'utility/backend.html', context)
