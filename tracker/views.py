from django.shortcuts import render, get_object_or_404,get_list_or_404,HttpResponse,redirect

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
    
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        print(customer_form.errors)
        if customer_form.is_valid():
            customer_form.save()
        return redirect('/')
            
    context = {'customer_form' : form}
    return render(request,'tracker/add_customer.html',context)

def list_customer(request, pk_customer):
    customer = get_object_or_404(Customer, id=pk_customer)
    context ={'customer':customer}
    return render(request,'tracker/list_customer.html',context)