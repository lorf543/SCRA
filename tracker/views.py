from django.shortcuts import render, get_object_or_404,get_list_or_404

from .models import Customer
# Create your views here.

def home(request):
    
    customer = get_list_or_404(Customer)
    
    context ={'customers':customer}
    return render(request,'tracker/home.html',context)


def customer_list(request):
    customer = get_object_or_404(Customer)
    context ={'customer':customer}
    return render(request,'',context)