from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains = searched)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    return render(request, 'app/search.html',{"searched":searched,"keys":keys,'products': products, 'cartItems':cartItems})

def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    context = {'form':form}
    return render(request,'app/register.html',context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: messages.info(request,'Tài khoản hoặc mật khẩu chưa chính xác!')
    context = {}
    return render(request,'app/login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('login')
def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context= {'products': products, 'cartItems':cartItems}
    return render(request, 'app/home.html', context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    context= {'items':items,'order':order,'cartItems':cartItems}
    return render(request, 'app/cart.html', context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    context= {'items':items,'order':order,'cartItems':cartItems}
    return render(request,'app/checkout.html', context)
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)
    if action == 'add':
        orderItem.quantity +=1
    elif action == 'remove':
        orderItem.quantity -=1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('added',safe=False)
def introduction(request):
    return render(request, 'app/introduction.html')
def contact(request):
    return render(request, 'app/contact.html')
def dell(request):
    return render(request, 'app/laptop/dell.html')
def acer(request):
    return render(request, 'app/laptop/acer.html')
def hp(request):
    return render(request, 'app/laptop/hp.html')
def asus(request):
    return render(request, 'app/laptop/asus.html')
def lenovo(request):
    return render(request, 'app/laptop/lenovo.html')
def dellinspiron(request):
    return render(request, 'app/ttsp/dellinspiron.html')
def dellXPS13(request):
    return render(request, 'app/ttsp/dellXPS13.html')
def dellalienware(request):
    return render(request, 'app/ttsp/dellalienware.html')
def AcerAspire(request):
    return render(request, 'app/ttsp/AcerAspire.html')
def AcerPredator(request):
    return render(request, 'app/ttsp/AcerPredator.html')
def Acerswift3(request):
    return render(request, 'app/ttsp/Acerswift3.html')
def Acerspin3(request):
    return render(request, 'app/ttsp/Acerspin3.html')
def Acernitro(request):
    return render(request, 'app/ttsp/Acernitro.html')
def Hpspectre(request):
    return render(request, 'app/ttsp/Hpspectre.html')
def Hpenvy(request):
    return render(request, 'app/ttsp/Hpenvy.html')
def Hppavilion(request):
    return render(request, 'app/ttsp/Hppavilion.html')
def Hpelitebook(request):
    return render(request, 'app/ttsp/Hpelitebook.html')
def Hpomen(request):
    return render(request, 'app/ttsp/Hpomen.html')
def Hpstream(request):
    return render(request, 'app/ttsp/Hpstream.html')
def Asuszenbook(request):
    return render(request, 'app/ttsp/Asuszenbook.html')
def Asusvivobook(request):
    return render(request, 'app/ttsp/Asusvivobook.html')
def AsusROG(request):
    return render(request, 'app/ttsp/AsusROG.html')
def AsusTUF(request):
    return render(request, 'app/ttsp/AsusTUF.html')
def AsusChrome(request):
    return render(request, 'app/ttsp/AsusChrome.html')
def AsusProart(request):
    return render(request, 'app/ttsp/AsusProart.html')
def LenovoThink(request):
    return render(request, 'app/ttsp/LenovoThink.html')
def LenovoIdea(request):
    return render(request, 'app/ttsp/LenovoIdea.html')
def LenovoYoga(request):
    return render(request, 'app/ttsp/LenovoYoga.html')
def LenovoLegion(request):
    return render(request, 'app/ttsp/LenovoLegion.html')
def LenovoChrome(request):
    return render(request, 'app/ttsp/LenovoChrome.html')
def LenovoX1(request):
    return render(request, 'app/ttsp/LenovoX1.html')
    