from django.shortcuts import render,redirect,get_object_or_404,HttpResponse

from scranotes.models import Notes
from tracker.models import Account,Address, Duplicates
from simple_history.utils import update_change_reason
from datetime import datetime
# Create your views here.


def all_account_history(request):
    history_account = Account.history.all()

    changes = []
    for i in range(1, len(history_account)):
        current = history_account[i]
        previous = history_account[i-1]
        fields_changed = []
        for field in current._meta.fields:
            field_name = field.name
            if getattr(current, field_name) != getattr(previous, field_name):
                fields_changed.append(field_name)
        changes.append((current, fields_changed))

    context = {
        'changes': changes,
    }
    return render(request, 'history/account_history.html', context)


def notes_history(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    history = note.history.all()
    return render(request, 'history/notes_history.html', {'note': note, 'history': history})


def all_history_notes(request):
    all_history = Notes.history.all()
    return render(request, 'history/all_history_notes.html', {'history': all_history})