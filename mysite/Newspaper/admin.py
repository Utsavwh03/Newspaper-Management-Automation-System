from django.contrib import admin
from Newspaper.models import Employee
from Newspaper.models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('name','address','email','phone_number')
admin.site.register(Customer,CustomerAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','address','email','phone_number','salary')
admin.site.register(Employee,EmployeeAdmin)
