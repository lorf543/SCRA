from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone


from .models import Inbox
from .forms import InboxForm
from tracker.models import Account

# Create your views here.

def list_inbox(request):
    inboxes = Inbox.objects.all()
    
    context = {'inboxes':inboxes}
    return render(request,'scrainbox/list_inbox.html',context)


def add_inbox(request, customer_id):
    inbox_form = InboxForm(request.POST)
    customer = get_object_or_404(Account, id=customer_id)
    print(inbox_form.errors)
    if request.method == "POST":
       inbox_form.is_valid()
       inbox = inbox_form.save(commit=False)
       inbox.customer = customer
       inbox.save()
       messages.success(request,'New inbox has been added')
       return redirect('detail_customer', customer.id)
        
    context = {'inbox_form':inbox_form}
    return render(request,'scrainbox/add_inbox.html',context)

def update_inbox(request, customer_id, inbox_id):
    customer = get_object_or_404(Account, id=customer_id)
    inbox = get_object_or_404(Inbox, id=inbox_id, customer=customer)
    
    if request.method == "POST":
        inbox_form = InboxForm(request.POST, instance=inbox)
        
        if inbox_form.is_valid():
            inbox = inbox_form.save(commit=False)
            inbox.updated_by  = request.user
            inbox.updated  = timezone.now().date()
            inbox.save()
            messages.success(
                request,'the inbox has been updated'
            )
        return redirect('detail_customer', customer.id)
    
    else:
        inbox_form = InboxForm(instance=inbox)

        
    context = {'inbox_form':inbox_form,}
    return render(request,'scrainbox/update_inbox.html',context)



