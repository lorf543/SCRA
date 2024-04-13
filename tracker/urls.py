from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),

    path('add-customer/',views.add_customer,name='add_customer'),
    path('detail-customer/<str:customer_id>/',views.detail_customer,name='detail_customer'),
    path('update-customer/<str:customer_id>/',views.update_customer,name='update_customer'),
    path('delete-customer/<str:customer_id>/',views.delete_customer,name='delete_customer'),
    #address path
    path('address-list/',views.address_list,name='address_list'),
    path('add-address/<int:customer_id>/', views.add_address, name='add_address'),
    path('upadate-address/<int:customer_id>/<int:address_id>/', views.upadate_address, name='upadate_address'),

]

htmx_urlpatterns = [
    path('check-customer/',views.check_customer,name='check_customer'),
]


urlpatterns += htmx_urlpatterns