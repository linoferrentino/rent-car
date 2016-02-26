from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^view_contracts$', views.view_contracts, name='view_contracts'),
    url(r'^view_invoices$', views.view_invoices, name='view_invoices'),
    url(r'^view_customers$', views.view_customers, name='view_customers'),
    url(r'^view_vehicles$', views.view_vehicles, name='view_vehicles'),

    url(r'^open_contract$', views.open_contract_view, name='open_contract'),
    url(r'^close_contract$', views.close_contract_view, name='close_contract'),
]
