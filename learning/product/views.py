from django.shortcuts import render

from .forms import ProductForm,UserSurveyForm,PhoneForm
from .models import Product,UserSurvey

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

def createSurveyForm(request):
    usersurvey = UserSurveyForm()
    if request.method == "POST":
        form = UserSurveyForm(request.POST)
        if form.is_valid():
            survey = UserSurvey(**form.cleaned_data)
            survey.save()
    return render(request,"product/SurveyForm.html",{"form":usersurvey})

def createPhoneView(request):
    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PhoneForm()
    return render(request,"product/createPhone.html",{"form":form})