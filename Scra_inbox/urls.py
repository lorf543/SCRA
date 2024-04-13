from django.urls import path

from . import views

urlpatterns = [
    path('list-inbox',views.list_inbox,name='list_inbox'),
]
