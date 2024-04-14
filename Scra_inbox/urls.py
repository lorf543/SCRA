from django.urls import path

from . import views

urlpatterns = [
    path('list-inbox',views.list_inbox,name='list_inbox'),
    path('add-inbox/<str:customer_id>/',views.add_inbox,name='add_inbox'),
    path('update-inbox/<str:customer_id>/<str:inbox_id>/',views.update_inbox,name='update_inbox'),
]
