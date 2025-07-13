from django.db import models

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR','HR'),
        ('Engineering','Engineering'),
        ('Marketing','Marketing'),
        ('Finance','Finance'),
        ('Sales','Sales'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=50,choices=DEPARTMENT_CHOICES)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    joining_date = models.DateField()

    class Meta:
        db_table = 'employees'
    
    def __str__(self):
        return self.name
