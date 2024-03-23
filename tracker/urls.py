from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('add-customer/',views.add_customer,name='add_customer'),
]

htmx_urlpatterns = [
    path('check-customer/',views.check_customer,name='check_customer'),
]


urlpatterns += htmx_urlpatterns