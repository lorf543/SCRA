from django.shortcuts import render,redirect,get_object_or_404,HttpResponse

from scranotes.models import Notes
# Create your views here.


def notes_history(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    history = note.history.all()
    return render(request, 'history/notes_history.html', {'note': note, 'history': history})


def all_history_notes(request):
    all_history = Notes.history.all()
    return render(request, 'history/all_history_notes.html', {'history': all_history})