from django.conf.urls import url
from networks import views

urlpatterns = [
    url(r'^addresses/available', views.available_addresses, name='networks_addresses_available'),
    url(r'addresses/assigned/(?P<slug>[\w.-]+)/$', views.assignments_csv, name='networks_addresses_assigned_csv'),
]

