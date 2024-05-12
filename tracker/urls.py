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
    path('update-address/<int:customer_id>/<int:address_id>/', views.update_address, name='update_address'),
    #letters 
    path('letters/mil/<int:customer_id>/',views.more_information,name='more_info'),
    path('letters/denial/<int:customer_id>/',views.denial_letter,name='denial_letter'),
    path('letters/approval/<int:customer_id>/',views.approval_letter,name='approval_letter'),

    path('export/',views.export_data, name='export_data'),

]

htmx_urlpatterns = [
    path('check-customer/',views.check_customer,name='check_customer'),
]


urlpatterns += htmx_urlpatterns