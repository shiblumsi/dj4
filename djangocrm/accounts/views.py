from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .filters import *
from .models import *
from .decorator import usauthenticated_users,allowed_users,admin_only



@usauthenticated_users
def register(request):
    form = Register_form()
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()


            return redirect('login')
    context = {
        'form':form,
    }
    return render(request,'register.html',context)





def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')

    context = {}
    return render(request,'login.html',context)



def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    customer = Customer.objects.all()
    order = Order.objects.all()
    total_order = order.count()
    total_customer = customer.count()
    pending = order.filter(status='Pending').count()
    delevered = order.filter(status= 'Delivered').count()




    context = {
        'customers':customer,
        'orders':order,
        'c_order':total_order,
        'ing':pending,
        'delevered':delevered,
        'total_customer':total_customer,


    }
    return render(request,'deshbord.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    order= customer.order_set.all()
    total_order = order.count()

    search_filter = formFilters(request.GET,queryset=order)
    order = search_filter.qs

    context = {
        'customer': customer,
        'total_order': total_order,
        'order': order,
        'search_filter': search_filter,
    }
    return render(request,'customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def product(request):
    product = Products.objects.all()
    context = {
        'product':product
    }
    return render(request,'products.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def users(request):
    orders = request.user.customer.order_set.all()
    context = {
        'orders':orders
    }
    return render(request,'userpage.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_order(request):
    c_form = Create_Order()
    if request.method == 'POST':
        form = Create_Order(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {
        'c_form':c_form
    }
    return render(request,'create_order.html',context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_order(request,pk):
    order = Order.objects.get(id=pk)

    c_form = Create_Order(instance=order)
    if request.method == 'POST':
        form = Create_Order(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {
        'c_form':c_form
    }
    return render(request,'create_order.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_remove(request,pk):
    order = Order.objects.get(id = pk)
    order.delete()
    return redirect('home')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def account_setting(request):
    customer = request.user.customer
    acc_form = Account_setting(instance=customer)
    if request.method == 'POST':
        acc_form = Account_setting(request.POST,request.FILES, instance=customer)
        if acc_form.is_valid():
            acc_form.save()
    context ={
        'acc_form':acc_form
    }
    return render(request,'account_setting.html',context)


