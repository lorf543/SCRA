from django.shortcuts import render, get_object_or_404,get_list_or_404,HttpResponse,redirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from openpyxl import Workbook

from .models import Account,Address,Duplicates
from .forms import CustomerForm,AddressForm,DuplicatesForm
from .filters import CustomerFilters
# Create your views here.

@login_required(login_url='login_user')
def export_data(request):
    queryset = Account.objects.all()  # Customize this queryset as needed

    # Create a new Workbook
    wb = Workbook()
    ws = wb.active

    # Add headers
    headers = [ 'customer_name','account_number','loan_type', 'open_state','acc_status','date_request','method_notification','date_open_acc','military_date','qualify','status_notes','first_review'
        ]  # Customize headers as needed
    ws.append(headers)

    # Add data rows
    for item in queryset:
        data_row = [item.customer_name, item.account_number, item.loan_type, item.open_state, item.acc_status, item.date_request,item.method_notification,item.date_open_acc,item.military_date, item.qualify,item.status_notes,item.first_review
        ]  # Customize fields as needed
        ws.append(data_row)

    # Save the workbook to a BytesIO object
    from io import BytesIO
    output = BytesIO()
    wb.save(output)
    output.seek(0)

    # Prepare HTTP response with Excel file
    response = HttpResponse(
        output.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    return response

@login_required(login_url='login_user')
def home(request):
    #customer = get_list_or_404(Account)
    filter = CustomerFilters(
        request.GET, queryset=Account.objects.all().order_by('-created')
    )
    context ={
    'customers':filter.qs,
    'filter':filter
    }
    return render(request, 'tracker/home.html',context)

def check_customer(request):
    account_number = request.POST.get('account_number')
    if Account.objects.filter(account_number=account_number).exists():
        return render(request,'partials/already_added.html',)
        
@login_required(login_url='login_user')
def add_customer(request):
    customer = Account.objects.all()
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        address_form = AddressForm(request.POST)
        
        if customer_form.is_valid() and address_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.added_by = request.user
            if customer.approved_date:
                customer.approved_by = request.user
                print(customer.approved_by)
                print(customer.customer.approved_date)
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
            

            
    context = {'customer_form' : customer_form, 'address_form':address_form,'customer':customer}
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
def update_customer(request, customer_id):
    customer = get_object_or_404(Account, id=customer_id)

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, instance=customer)
        
        if customer_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.updated_by = request.user
            if customer.qualify == True:
                customer.approved_by = request.user
                customer.approved_date = timezone.now().date()
            else:
                customer.approved_by = None
                customer.approved_date = None                

            customer.save()
            return redirect('detail_customer', customer.id)
    else:
        customer_form = CustomerForm(instance=customer)
            
    context = {'customer_form': customer_form, 'customer': customer}
    return render(request, 'tracker/update_customer.html', context)

    

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

#________________________Duplicates____________________

@login_required(login_url='login_user')
def add_duplicate(request,customer_id):
    customer = get_object_or_404(Account, id=customer_id)

    if request.method == 'POST':
        form_duplicates = DuplicatesForm(request.POST)

        if form_duplicates.is_valid():
            duplicates = form_duplicates.save(commit=False)
            duplicates.customer = customer
            duplicates.added_by = request.user
            duplicates.save()
                
    else:
        form_duplicates = DuplicatesForm()

    context = {'form_duplicates':form_duplicates}
    return render(request,'duplicates/add_duplicate.html',context)

@login_required(login_url='login_user')
def update_duplicate(request,customer_id,duplicate_id):
    customer = get_object_or_404(Account, id=customer_id)
    duplicate = get_object_or_404(Duplicates, id=duplicate_id, customer=customer)

    if request.method == 'POST':
        form_duplicates = DuplicatesForm(request.POST,instance=duplicate)

        if form_duplicates.is_valid():
            duplicates = form_duplicates.save(commit=False)
            duplicates.updated_by = request.user
            duplicates.update = timezone.now().date()
            duplicates.save()
            messages.success(
                request,'the duplicated note has been updated'
            )   
        return redirect('detail_customer', customer.id)
    else:
        form_duplicates = DuplicatesForm(instance=duplicate)

    context = {'form_duplicates':form_duplicates,'customer':customer,'duplicate':duplicate}
    return render(request,'duplicates/add_duplicate.html',context)

@login_required(login_url='login_user')
def delete_duplicate(request,customer_id,duplicate_id):
    customer = get_object_or_404(Account, id=customer_id)
    duplicate = get_object_or_404(Duplicates, id=duplicate_id, customer=customer)

    if request.method=='POST':
        duplicate.delete()
        messages.success(
            request,'The note duplicated has been deleted!'
        )
        return redirect('detail_customer', customer.id)

    context = {'customer':customer, 'duplicate':duplicate}
    return render(request,'duplicates/delete_duplicate.html',context)

#________________________Pending__________________

def list_pending(request):
    customers = Account.objects.all()

    context = {'customers':customers}
    return render(request,'pending/pending_list.html',context)
