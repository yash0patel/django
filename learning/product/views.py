from django.shortcuts import render

from .forms import ProductForm
from .models import Product

def createProduct(request):
    productForm = ProductForm()
    if request.method == "POST":
        print("form subbmited....")
        form = ProductForm(request.POST)
        if  form.is_valid():
            print("form is valid...")
            print(form.cleaned_data)
            product = Product(**form.cleaned_data)
            product.save()
    return render(request,"product/createProduct.html",{"form": productForm})