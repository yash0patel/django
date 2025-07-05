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