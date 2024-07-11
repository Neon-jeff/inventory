from django.shortcuts import render,redirect
from .models import Item
from django.contrib import messages

# Create your views here.


def AppPage(request):
    # get all items
    items=Item.objects.all()
    if request.method=='POST':
        data=request.POST
        image=request.FILES['file']
        Item.objects.create(name=data['name'],description=data['description'],unit_price=data['unit_price'],quantity=data['quantity'],image=image,barcode_id=data['barcode'])
        messages.success(request,'New Inventory Added')
    return render(request,'index.html',{"items":items})

def DeleteItem(request,pk):
    item =Item.objects.get(id=pk)
    item.delete()
    messages.success(request,'Item deleted successfully')
    return redirect('app')

def UpdateItem(request,pk):
    if request.method=='POST':
        data=request.POST
        item=Item.objects.filter(id=pk)[0]
        item.name=data['name']
        item.unit_price=data['unit_price']
        item.description=data['description']
        item.quantity=data['quantity']
        item.save()
        messages.success(request,f'{item.name} updated successfully')
        return redirect('app')