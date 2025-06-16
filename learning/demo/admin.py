from django.contrib import admin
from .models import Product,Student,Employee,SwiggyUser,Wallet,Teams,Tournament
# Register your models here.
admin.site.register(Product)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(SwiggyUser)
admin.site.register(Wallet)
admin.site.register(Teams)
admin.site.register(Tournament)
