from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Vehicle, Customer, Invoice, Contract

def index(request):
    context = {'clients_list': {}}
    return render(request, 'rent/welcome.html', context)

def open_contract_view(request):
    #to open a contract I have to make a list of customers and vehicles
    list_customers = Customer.objects.all()
    list_vehicles = Vehicle.objects.all()

    context = {'customers_list': list_customers, 'vehicles_list': list_vehicles}
    return render(request, 'rent/open_contract.html', context)


def close_contract_view(request):
    ht = HttpResponse("da fare... chiudi contratto")
    return ht

def view_contracts(request):
    ht = HttpResponse("Qui ci sono i contratti")
    return ht

def view_invoices(request):
    ht = HttpResponse("Qui ci sono le fatture")
    return ht

def view_customers(request):
    ht = HttpResponse("Qui ci sono i clienti")
    return ht

def view_vehicles(request):
    ht = HttpResponse("Qui ci sono i mezzi")
    return ht
