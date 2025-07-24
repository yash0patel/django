from django import forms
from .models import UserSurvey,Phone,Contact

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


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ["brand","model","price","description","stock"]
        labels = {
            'brand' : 'Brand',
            'model' : 'Model',
            'price' : 'Price',
            'description' : 'Description',
            'stock' : 'Stock'
        }
        widgets = {
            'brand' : forms.TextInput(attrs={'placeholder' : 'Enter the brand name'}),
            'model' : forms.TextInput(attrs={'placeholder' : 'Enter the model name'}),
            'price' : forms.NumberInput(attrs={'placeholder' : 'Enter the price'}),
            'description' : forms.Textarea(attrs={'placeholder' : 'Enter the description'}),
            'stock' : forms.NumberInput(attrs={'placeholder' : 'Enter the stock'}),
        }
        error_messages = {
            'brand': {
                'required': "Brand name is required",
                'max_length': "Brand name is too long"
            },
            'model': {
                'required': "Model name is required",
                'max_length': "Model name is too long"
            },
            'price': {
                'required': "Price is required",
                'invalid': "Enter a valid number for price"
            },
            'description': {
                'required': "Description is required",
            },
            'stock': {
                'required': "Stock value is required",
                'invalid': "Enter a valid stock quantity"
            }
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 100:
            raise forms.ValidationError("Price must be greater than zero.")
        return price   
    
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError("Stock cannot be negative.")
        return stock 
    

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'