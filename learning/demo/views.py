from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.db.models import Q
# Create your views here.


def home(request):
    return HttpResponse("Home")

def aboutus(request):
    coumpany={
        "name":"tcs",
        "location":"delhi",
        "founder":"tata"
    }
    return render(request,"aboutus.html",{'coumpany':coumpany})

def contactus(request):
    user = {
        "name" : "amit",
        "age" : 18,
        "city" : "ahm",
        "salary" : 1000
    }
    return render(request,"contactus.html",{'user':user})

def studentList(request):
    # students = {
    #     "student":["yash","ram","raj","dev"]
    # }

    students = ["yash","ram","raj","dev"]
    return render(request,"studentlist.html",{'students':students})

# def productList(request):
#     products = [
#         {
#             "name":"iphone1",
#             "price":2500,
#             "qty":2,
#             "color":"red"
#         },
#         {
#             "name":"ipad",
#             "price":2700,
#             "qty":1,
#             "color":"blue"
#         },
#         {
#             "name":"charger",
#             "price":1000,
#             "qty":3,
#             "color":"green"
#         },
#         {
#             "name":"pr2",
#             "price":3000,
#             "qty":4,
#             "color":"black"
#         }
#     ]

#     return render(request,"productList.html",{'products':products})

def getProducts(request):
    # products = Product.objects.all().values_list('name','price','stock','color')

    # products = Product.objects.get(pk=1)
    # print(products)

    # products = Product.objects.filter(status = True,name = "xyz").values()
    # print("products : ",products)
    # return HttpResponse("product")

    # products = Product.objects.all()[:1].values_list('name','price','stock','color')
    # products = Product.objects.all().order_by("-stock").values_list('name','price','stock','color')
    
    # products = Product.objects.exclude(field_name = "color").values()
    
    # hookups
    products = Product.objects.filter(name__contains="p").values()
    products = Product.objects.filter(name__icontains="P").values()
    products = Product.objects.filter(price__gt=1200).values()
    products = Product.objects.filter(price__gte=1000).values()
    products = Product.objects.filter(color__in=["silver","red"]).values()
    products = Product.objects.filter(price__range=(1200,30000)).values() 
    products = Product.objects.filter(name__istartswith="I").values()

    products = Product.objects.filter(Q(name = "abc") | Q(price__gte=1000) & Q(name__contains="p")).values()
    products = Product.objects.filter(~Q(name = "abc") | Q(price__gte=1000)).values()

    print("products : ",products)

    return render(request,"productList.html",{'products':products})
