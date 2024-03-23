from django.shortcuts import render, get_object_or_404,get_list_or_404,HttpResponse

from .models import Customer
from .forms import CustomerForm
# Create your views here.

def home(request):
    
    customer = get_list_or_404(Customer)
    
    context ={'customers':customer}
    return render(request,'tracker/home.html',context)


def customer_list(request):
    customer = get_object_or_404(Customer)
    context ={'customer':customer}
    return render(request,'',context)


def check_customer(request):
    account_number = request.POST.get('account_number')
    print(account_number)
    if Customer.objects.filter(account_number=account_number).exists():
        return render(request,'partials/already_added.html',)
        

def add_customer(request):
    form = CustomerForm()
    context = {'customer_form' : form}
    return render(request,'tracker/add_customer.html',context)