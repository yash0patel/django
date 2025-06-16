from django.db import models

# Create your models here.
class Product(models.Model):
    rating_choice =[
        (1, '1 Star'), 
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=50,null=True,blank=True)
    status = models.BooleanField(default=True,null=True,)
    ratings = models.IntegerField(choices=rating_choice,default=1,null=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['stock']

    def __str__(self):
        return self.name
    

class Student(models.Model):
    gender_choice = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    course_choice = [
        (1, 'B.Tech'),
        (2, 'BCA'),
        (3, 'M.Tech'),
        (4, 'MCA'),
        (5, 'MBA'),
    ]

    student_id = models.CharField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=gender_choice, default='M', null=True)
    course = models.IntegerField(choices=course_choice)
    dob = models.DateField(null=True, blank=True)
    enrollment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'student'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['student_id']

    def __str__(self):
        return self.name



class Employee(models.Model):
    gender_choice = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    emp_id = models.CharField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=gender_choice,default='M',null=True)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employee'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['id']

    def __str__(self):
        return self.name


class Wallet(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table = "wallet"

    def __str__(self):
        return self.name

class SwiggyUser(models.Model):
    name = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    wallet = models.OneToOneField(Wallet,on_delete=models.CASCADE,related_name="swiggy_user")

    class Meta:
        db_table = "swiggy_user"

    def __str__(self):
        return self.name
    
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)

    class Meta:
        db_table = "tournament"

    def __str__(self):
        return self.name
    
class Teams(models.Model):
    name = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE,related_name="teams")

    class Meta:
        db_table = "teams"

    def __str__(self):
        return self.name
