from django.shortcuts import render, get_object_or_404,get_list_or_404,HttpResponse,redirect

from .models import Customer,Address
from .forms import CustomerForm

from django.utils import timezone
# Create your views here.



def home(request):
    customer = get_list_or_404(Customer)
    context ={'customers':customer}
    return render(request, 'tracker/home.html',context)


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
        if  customer_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.added_by = request.user
            customer.save()
        return redirect('/')
            
    context = {'customer_form' : form}
    return render(request,'tracker/add_customer.html',context)

def dl_note(customer,request):
    if customer.danial_date:
                customer.denial_by = request.user
                if customer.military_date:
                    customer.denial_note =  f"""
                        SCRA account review. we have check form military
                        date {customer.military_date.strftime('%m/%d/%Y')}. and the open account date {customer.date_open_acc.strftime('%m/%d/%Y')}.
                        account does not qualify for SCRA benefits. 
                        Denial Date.
                    """
                else:
                    customer.denial_note = f"""
                        SCRA account review. we have check form military
                        date "N/A. and the open account date {customer.date_open_acc.strftime('%m/%d/%Y')}.
                        account does not qualify for SCRA benefits. 
                        Denial Date.
                    """


def update_customer(request,customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST,instance=customer)
        print(customer_form.errors)
        if customer_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.updated_by = request.user
            customer.updated = timezone.now().date()
            dl_note(customer,request)
            customer.save()
        return redirect('/')
    else:
        customer_form = CustomerForm(instance=customer)
            
    context = {'customer_form' : customer_form,'customer':customer}
    return render(request,'tracker/update_customer.html',context)

def detail_customer(request, pk_customer):
    customer = get_object_or_404(Customer, id=pk_customer)
    context ={'customer':customer}
    return render(request,'tracker/detail_customer.html',context)


#________________________Adress________________________________
def return_letter(request):
    address = Address.objects.all()
    context = {'address':address}
    return render(request,'return/return_tracker.html',context)