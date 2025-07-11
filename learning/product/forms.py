from django import forms
from .models import UserSurvey

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100,label='Product Name')
    price = forms.IntegerField(label='Price')
    stock = forms.IntegerField(label='Stock')
    description = forms.CharField(widget=forms.Textarea,label='Decription')

class UserSurveyForm(forms.Form):
    name = forms.CharField(max_length=100,label='Full Name')
    gender = forms.ChoiceField(
        choices=UserSurvey.GENDER_CHOICES,
        label='Gender',
        widget=forms.RadioSelect
    )
    products = forms.MultipleChoiceField(
        choices=UserSurvey.PRODUCTS_CHOICES,
        label='Select Products',
        widget=forms.CheckboxSelectMultiple
    )
    feedback = forms.CharField(
        label='Your Feedback',
        required=False,
        widget=forms.Textarea()
    )
    has_coupon = forms.BooleanField(
        label='Do you have a coupon?',
        required=False
    )