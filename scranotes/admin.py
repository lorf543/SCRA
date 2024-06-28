from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Notes

# Register your models here.

class NotesHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'note_title']
    history_list_display = ['note_title']
    search_fields = ['note_title']

admin.site.register(Notes,NotesHistoryAdmin)

