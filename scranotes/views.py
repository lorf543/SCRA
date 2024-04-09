from django.shortcuts import render,redirect

from .models import Notes
from .forms import NotesForm
# Create your views here.


def note_scra_list(request):
    search_query = request.GET.get('q', '')
    notes = Notes.objects.filter(note_title__icontains=search_query)
    
    context = {'notes':notes,'search_query':search_query}
    return render(request,'scranotes/list_notes.html',context)

def note_scra_add(request):
    form = NotesForm()
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note=form.save(commit=False)
            note.added_by = request.user
            note.save()
            
            return redirect('list_notes')
    context = {'form':form,}
    return render(request,'scranotes/add_notes.html',context)