from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Notes
from .forms import NotesForm
# Create your views here.

@login_required(login_url='login_user')
def note_scra_list(request):
    search_query = request.GET.get('q', '')
    notes = Notes.objects.filter(note_title__icontains=search_query)
    
    context = {'notes':notes,'search_query':search_query}
    return render(request,'scranotes/list_notes.html',context)

@login_required(login_url='login_user')
def note_scra_add(request):
    form = NotesForm()
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note=form.save(commit=False)
            note.added_by = request.user
            note.save()
            messages.success(
                request, 'New note has been added'
            )
            return redirect('list_notes')
    context = {'form':form,}
    return render(request,'scranotes/add_notes.html',context)

@login_required(login_url='login_user')
def note_scra_update(request,note_id):
    note = get_object_or_404(Notes, id=note_id)
    if request.method == 'POST':
        form = NotesForm(request.POST,instance=note)
        if form.is_valid():
            note=form.save(commit=False, )
            note.added_by = request.user
            note.save()
            messages.success(
                request, 'The was updated correctly!'
            )
            return redirect('list_notes')
    else:
        form = NotesForm(instance=note)
    context = {'form':form,}
    return render(request,'scranotes/update_notes.html',context)

@login_required(login_url='login_user')
def note_scra_delete(request,note_id):
    note = get_object_or_404(Notes, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('list_notes')
