from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    
    class Meta:
        db_table = "product1"
        
    def __str__(self):
        return self.name    

class UserSurvey(models.Model):
    GENDER_CHOICES = [('male','male'),('female','female')]
    PRODUCTS_CHOICES = [('pr1','pr1'),('pr2','pr2'),('pr3','pr3')]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    products = models.CharField(max_length=200)    
    feedback = models.TextField(blank=True)
    has_coupon = models.BooleanField(default=False)

    class Meta:
        db_table = "usersurvey"

class Phone(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    stock = models.PositiveIntegerField()

    class Meta:
        db_table = 'phone'

    def __str__(self):
        return self.model

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        db_table = 'contact'