from django.shortcuts import render


from .models import Inbox

# Create your views here.

def list_inbox(request):
    inboxes = Inbox.objects.all()
    
    context = {'inboxes':inboxes}
    return render(request,'scrainbox/list_inbox.html',context)