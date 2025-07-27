from django.db import models

class employee1(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=50)
    joining = models.BooleanField()
    date = models.DateField()

    class Meta:
        db_table = 'employee1'