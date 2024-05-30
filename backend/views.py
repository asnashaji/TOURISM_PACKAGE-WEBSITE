from django.shortcuts import render,redirect
from backend.models import  categorydb,packagedb,daysdb
from frontend.models import contactdb,ratedb,details
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def index(req):
    return render(req,"index.html")
def category(req):
    return render(req,"category.html")
def cat(request):
    if request.method == "POST":
        na = request.POST.get('names')
        dis = request.POST.get('disp')
        img = request.FILES['images']
        obj = categorydb(name=na,discription=dis,image=img)
        obj.save()
        messages.success(request,"category added successfully...")
        return redirect(category)
def pack(req):
    return render(req,"packages.html")
def packages(req):
    if req.method == "POST":
        st = req.POST.get('states')
        cy = req.POST.get('citys')
        ra = req.POST.get('rates')
        ho = req.POST.get('hotels')
        ac = req.POST.get('activs')
        dis = req.POST.get('disps')
        img = req.FILES['images']
        obj = packagedb(state=st,city=cy,rate=ra,hotel=ho,activitie=ac, disp=dis, image=img)
        obj.save()
        messages.success(req,"package  added successfully...")

        return redirect(pack)
def viewcat(req):
    data=categorydb.objects.all()
    return render(req,"viewcat.html",{"data":data})
def viewpack(req):
    data=packagedb.objects.all()
    return render(req,"viewpack.html",{"data":data})
def viewcont(req):
    data=contactdb.objects.all()
    return render(req,"contactview.html",{"data":data})

def viewpay(req):
    data=ratedb.objects.all()
    return render(req,"PAYMENTVIEW.html",{"data":data})


def viewcustamize(req):
    data=details.objects.all()
    return render(req,"custamizeview.html",{"data":data})

def deletepage(req,dataid):
    de= packagedb.objects.filter(id=dataid)
    de.delete()
    messages.error(req, "product deleted")
    return redirect(viewpack)

def deleteconct(req,dataid):
    de= contactdb.objects.filter(id=dataid)
    de.delete()
    messages.error(req,"contact deleted")
    return redirect(viewcont)

def deletecat(req,dataid):
    de= categorydb.objects.filter(id=dataid)
    de.delete()
    messages.error(req, "category deleted ")
    return redirect(viewcat)


def packedit(req,dataid):
    pack=packagedb.objects.get(id=dataid)
    return render(req,"editpack.html",{"pack":pack})

def packupdate(req,dataid):
    if req.method=="POST":
        st = req.POST.get('states')
        cy = req.POST.get('citys')
        ra = req.POST.get('rates')
        ho = req.POST.get('hotels')
        ac = req.POST.get('activs')
        ds = req.POST.get('disps')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)

        except MultiValueDictKeyError:
            file = packagedb.objects.get(id=dataid).image
            packagedb.objects.filter(id=dataid).update(state=st,city=cy,rate=ra,hotel=ho, activitie =ac,disp=ds)
            messages.success(req, "package update successfully...")
            return redirect(viewpack)





def catedit(req,dataid):
    cat=categorydb.objects.get(id=dataid)
    return render(req,"editcat.html",{"cat":cat})

def catupdate(req,dataid):
    if req.method == "POST":
        na = req.POST.get('names')
        dis = req.POST.get('disps')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)

        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).image
            categorydb.objects.filter(id=dataid).update(name=na,discription=dis,image=file)
            messages.success(req,"product add sucessfully")
            return redirect(viewcat)



def days(req):
    return render(req,"days.html")
def day(req):
    if req.method == "POST":
        st = req.POST.get('states')
        cty = req.POST.get('citys')
        dys = req.POST.get('days')
        act = req.POST.get('actv')
        des = req.POST.get('dest')
        obj = daysdb(state=st,city=cty,days=dys,activity1=act,disp1=des,)
        obj.save()
        return redirect(days)


