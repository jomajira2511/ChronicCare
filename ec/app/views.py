from django.shortcuts import redirect, render
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from . models import Customer, Product
from django.db.models import Count, Q
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages


# Create your views here.

def home (request):
    return render(request,"app/home.html")

def about (request):
    return render(request,"app/about.html")

def contact (request):
    return render(request,"app/contact.html")

class CategoryView(View):
    def get (self, request,val):
        product = Product.objects.filter(categoria=val)
        title = Product.objects.filter(categoria=val).values('titulo')
        return render(request,"app/category.html", locals())
    
class CategoryTitle(View):
    def get (self, request,val):
        product = Product.objects.filter(titulo=val)
        title = Product.objects.filter(categoria=product[0].categoria).values('titulo')
        return render(request,"app/category.html",locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())    

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El usuario ha sido registrado con exito")
        else:
            messages.warning(request,"Datos incorrectos")
        return render(request, 'app/customerregistration.html', locals())

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html',locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usuario = request.user
            nombre = form.cleaned_data['nombre'] 
            fecha = form.cleaned_data['fecha']  
            bitacora  = form.cleaned_data['bitacora'] 
            
            reg = Customer(usuario=usuario,nombre=nombre,fecha=fecha,bitacora=bitacora)
            reg.save()
            messages.success(request,"Bitacora, guardada con exito")
        else:
            messages.warning(request,"Error al guardar los datos")
        return render(request, 'app/profile.html',locals())
    
    
def address(request):
    add = Customer.objects.filter(usuario=request.user)
    return render(request, 'app/address.html', locals())


class updateAddress(View):
    def get(self,request,pk):
        add= Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'app/updateAddress.html', locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():   #permite agregar nuevos valores 
            add = Customer.objects.get(pk=pk)
            add.nombre = form.cleaned_data['nombre'] 
            add.fecha = form.cleaned_data['fecha']  
            add.bitacora = form.cleaned_data['bitacora'] 
            add.save()
            messages.success(request,"Bitacora guardada con exito")
        else:
            messages.warning(request,"Error al guardar los datos")
        return redirect("address") 
    
    
def search (request):
    query = request.GET['search']
    product =  Product.objects.filter(Q(titulo__icontains=query))
    return render(request, "app/search.html", locals())