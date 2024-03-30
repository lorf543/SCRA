from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('add-customer/',views.add_customer,name='add_customer'),
    path('detail-customer/<str:pk_customer>/',views.detail_customer,name='detail_customer'),
    path('update-customer/<str:customer_id>/',views.update_customer,name='update_customer'),
    
    path('return-letter/',views.return_letter,name='return-letter'),
]

htmx_urlpatterns = [
    path('check-customer/',views.check_customer,name='check_customer'),
]


urlpatterns += htmx_urlpatterns