from django.urls import path
from . import views


urlpatterns = [
    path('list/',views.note_scra_list,name='list_notes'),
    path('add/',views.note_scra_add,name='add_notes'),
    path('update/<str:note_id>',views.note_scra_update,name='update_notes'),
    path('delete/<str:note_id>',views.note_scra_delete,name='delete_notes'),
]