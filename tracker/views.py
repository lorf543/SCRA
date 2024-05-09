from django.shortcuts import render, get_object_or_404,get_list_or_404,HttpResponse,redirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import Account,Address
from .forms import CustomerForm,AddressForm
Account
# Create your views here.


@login_required(login_url='login_user')
def home(request):
    customer = get_list_or_404(Account)
    context ={'customers':customer}
    return render(request, 'tracker/home.html',context)

def check_customer(request):
    account_number = request.POST.get('account_number')
    if Account.objects.filter(account_number=account_number).exists():
        return render(request,'partials/already_added.html',)
        
@login_required(login_url='login_user')
def add_customer(request):
    
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        address_form = AddressForm(request.POST)
        
        if  customer_form.is_valid() and address_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.added_by = request.user
            customer.save()

            address = address_form.save(commit=False)
            address.customer = customer
            address.made_by = request.user
            address.save()
            
            messages.success(
                request, 'New entry of a customer has been added to SCRA tracker') 
            return redirect('/')
    else:
        customer_form = CustomerForm()
        address_form = AddressForm()
            

            
    context = {'customer_form' : customer_form, 'address_form':address_form}
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

@login_required(login_url='login_user')
def update_customer(request,customer_id):
    customer = get_object_or_404(Account, id=customer_id)

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST,instance=customer)
        
        #print(customer_form.errors)
        if customer_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.updated_by = request.user
            customer.updated = timezone.now().date()
            dl_note(customer,request)
            customer.save()
        return redirect('detail_customer',customer.id)
    else:
        customer_form = CustomerForm(instance=customer)
            
    context = {'customer_form' : customer_form,'customer':customer}
    return render(request,'tracker/update_customer.html',context)

@login_required(login_url='login_user')
def detail_customer(request, customer_id):
    customer = get_object_or_404(Account, id=customer_id)
    

    context ={'customer':customer,}
    return render(request,'tracker/detail_customer.html',context)

@login_required(login_url='login_user')
def delete_customer(request, customer_id):
    customer = get_object_or_404(Account, id=customer_id)
    if request.method == "POST":
        customer.delete()
        messages.success(
            request,'The account number associated to this customer has been deleted')
        return redirect('/')


#________________________Address________________________________

def address_list(request):
    customer = Account.objects.all()
    address = Address.objects.all()
    
    context = {'address':address,'customer':customer}
    return render(request,'return/return_tracker.html',context)

@login_required(login_url='login_user')
def add_address(request, customer_id):
    customer = get_object_or_404(Account, id=customer_id)
    address_form = AddressForm()
    
    if request.method == 'POST':
        address_form = AddressForm(request.POST)

        if address_form.is_valid():
            address = address_form.save(commit=False)
            address.customer = customer
            address.added_by = request.user
            address.save()
            return redirect('detail_customer', customer.id)
    else:
        address_form = AddressForm()
        
    context = {'address_form':address_form,'customer':customer}
    return render(request,'return/add_address.html',context)

@login_required(login_url='login_user')
def update_address(request, customer_id, address_id):
    customer = get_object_or_404(Account, id=customer_id)
    address = get_object_or_404(Address, id=address_id, customer=customer)
    
    if request.method == 'POST':
        address_form = AddressForm(request.POST, instance= address)
        
        if address_form.is_valid():
            address = address_form.save(commit=False)
            address.updated_by = request.user
            address.update = timezone.now().date()
            address.save()
            messages.success(
                request,'the address has been updated'
            )
        return redirect('detail_customer', customer.id)
    else:
        address_form = AddressForm(instance= address)
        
    context = {'address_form': address_form,'customer':customer,'address':address}
    return render(request,'return/update_address.html',context)

@login_required(login_url='login_user')           
def delete_address(request, address_id):
    address = get_object_or_404(Address, id=address_id)
    if request.method == "POST":
        address.delete()
        return redirect('detail_customer')
    return

#_______________________Letters___________________________________
@login_required(login_url='login_user')  
def more_information(request, customer_id):
    customer = get_object_or_404(Account, id=customer_id)

    context = {'customer': customer,}
    return render(request,'letter/more_information.html',context)

@login_required(login_url='login_user')  
def denial_letter(request, customer_id):
    customer = get_object_or_404(Account, id=customer_id)

    context = {'customer': customer,}
    return render(request,'letter/Denial_letter.html',context)

@login_required(login_url='login_user')
def approval_letter(request, customer_id):
    customer = get_object_or_404(Account, id=customer_id)

    context = {'customer': customer,}
    return render(request,'letter/approval_letter.html',context)