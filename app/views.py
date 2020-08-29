from django.shortcuts import render,redirect
from .models import Restaurant,Dises,Transaction
import json
import datetime
from django.http import HttpResponse
import ast

# Create your views here.

def index(request):
    return render(request,'login.html')

def home(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    if username == 'prakash9724' and password == '9712132751':
        obj=Restaurant.objects.all()
        return render(request,'index.html',{"data":obj})
    else:
        return render(request,'login.html')

def add(request):
    if request.method=='POST':
        print("post method++++++++++++++")
        restaurant=request.POST.get('res_name')
        location=request.POST.get('location')
        print(restaurant,location)
        Restaurant.objects.create(
            restaurant_name=restaurant,
            location=location
        )
        obj=Restaurant.objects.all()
        return redirect('/')

def dises(request,pk):
    res=Restaurant.objects.get(id=pk)
    response=Dises.objects.filter(res_id=pk).exists()
    if response:
        obj=Dises.objects.filter(res_id=pk)
        objs=Transaction.objects.filter(res_id=pk)
        
        li=[]
        data={}
        data1={}
        for share in objs:
            li.append(ast.literal_eval(share.dises))

    
        for i in li:
            for key,value in i.items():
                if int(key) not in data:
                    data[int(key)]=int(value)
                else:
                    data[int(key)]+=int(value)

    
        li2=[]
        li3=[['Task', 'Hours per Day']]
        print(data)
        best=0
        for key,value in data.items():
            if Dises.objects.filter(id=key).exists():
                dobj=Dises.objects.get(id=key)
                data1[value]=dobj.dises_name
                li2.append(value)
                li3.append([dobj.dises_name,value])
        if bool(data1):
            best=data1[max(li2)]

        
        return render(request,'dises.html',{'dises':data1,'best':best,'listdata':json.dumps(li3),"id":pk,"data":obj,'res':res})
    else:
        
        return render(request,'dises.html',{"id":pk,'res':res})
        

def addDis(request):
    if request.method=='POST':
        print("post method++++++++++++++")
        pk=request.POST.get('res_id')
        dis_name=request.POST.get('dis_name')
        price=request.POST.get('price')

        Dises.objects.create(
            res_id=pk,
            dises_name=dis_name,
            dises_price=price
        )
        obj=Dises.objects.filter(res_id=pk)
        return redirect('/dises/'+pk)


def edit(request,pk):
        obj=Restaurant.objects.get(id=pk)
        return render(request,'edit_restaurant.html',{'obj':obj,'id':pk})

def editDises(request,res_id,pk):
        obj=Dises.objects.get(id=pk)
        return render(request,'edit_dises.html',{'obj':obj,'res_id':res_id,'id':pk})

def editSave(request):
    if request.method=='POST':
        id=request.POST.get('id')
        res_name=request.POST.get('res_name')
        location=request.POST.get('location')
        obj=Restaurant.objects.get(id=id)
        obj.restaurant_name=res_name
        obj.location=location
        obj.save()
        return redirect('/')

def editSaveDises(request):
    if request.method=='POST':
        id=request.POST.get('id')
        res_id=request.POST.get('res_id')
        dis_name=request.POST.get('dis_name')
        price=request.POST.get('price')
        obj=Dises.objects.get(id=id)
        obj.dises_name=dis_name
        obj.dises_price=price
        obj.save()
        return redirect('/dises/'+res_id)


def delete(request,pk):
        Restaurant.objects.get(id=pk).delete()
        Dises.objects.filter(res_id=pk).delete()
        Transaction.objects.filter(res_id=pk).delete()
        return redirect('/')


def deleteDises(request,res_id,pk):
        Dises.objects.get(id=pk).delete()
        return redirect('/dises/'+str(res_id))


def billing(request,res_id):
    obj=Dises.objects.filter(res_id=res_id)
    res=Restaurant.objects.get(id=res_id)
    # objs=Transaction.objects.filter(res_id=res_id)
    # li=[]
    # data={}
    # data1={}
    # for share in objs:
    #     li.append(ast.literal_eval(share.dises))

    
    # for i in li:
    #     print(i)
    #     for key,value in i.items():
    #         if int(key) not in data:
    #             data[int(key)]=int(value)
    #         else:
    #             data[int(key)]+=int(value)

    

    # print(data)
    # for key,value in data.items():
    #     dobj=Dises.objects.get(id=key)
    #     data1[dobj.dises_name]=value

    # print(data1)

    return render(request,'billing.html',{"obj":obj,"res_id":res_id,"res":res,'date':str(datetime.datetime.today().strftime ('%d-%m-%Y'))})

def billData(request):
    data={}
    data1={}
    res_id=request.POST.get('res_id')
    for key in request.POST:
        if key != 'csrfmiddlewaretoken' and key != 'res_id':
            data[key]=request.POST.get(key)

    if bool(data):
        Transaction.objects.create(
            res_id=res_id,
            dises=data,
            date=str(datetime.datetime.today().strftime ('%d-%m-%Y'))
        )   
    for key in request.POST:
        if key != 'csrfmiddlewaretoken' and key != 'res_id':
            li=[]
            obj=Dises.objects.get(id=key)
            li.append(request.POST.get(key))
            li.append(obj.dises_price)
            data1[obj.dises_name]=li

    print("data1:++++++",data1)
    return  HttpResponse(json.dumps(data1), content_type="application/json")
           
def billview(request):
    return render(request,'billview.html')

