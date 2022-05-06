from django.shortcuts import render,redirect
from .models import shop
from .forms import ModeForm

# Create your views here.
def demo(request):
    obj=shop.objects.all()
    return render(request,'home.html',{'obj':obj})

def detail(request,prod_id):
    obj2 = shop.objects.get(id=prod_id)
    return render(request,'detail.html',{'obj2':obj2})

def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        img = request.FILES['img']
        s = shop(name=name,desc=desc,price=price,img=img)
        s.save()
        print("product added")
    return render(request,'add_product.html')

def update(request,id):
    obj = shop.objects.get(id=id)
    form = ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'obj':obj,'form':form})

def delete(request,id):
    if request.method == "POST":
        ob = shop.objects.get(id=id)
        ob.delete()
        return redirect('/')
    return render(request,'delete.html')

