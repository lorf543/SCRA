from django.urls import path
from . import views

urlpatterns = [
    path('notes/<int:note_id>/history/', views.notes_history, name='notes_history'),
    path('history/', views.all_history_notes, name='all_history'),
]
