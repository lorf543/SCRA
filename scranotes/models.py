from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Notes(models.Model):
    note_title = models.CharField(max_length=50)
    note = models.TextField()

    created = models.DateTimeField(auto_now_add=True, null=True, blank = True)
    updated = models.DateTimeField(null=True, blank = True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='note_add', null=True, blank = True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='noter_update',null=True, blank = True)


    
    class Meta:
        verbose_name = 'Note'
        
    def __str__(self):
        return self.note_title
    