from django.contrib import admin
from .models import Employee,Bank_Branches
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id']
    
@admin.register(Bank_Branches)
class Bank_BranchesAdmin(admin.ModelAdmin):
    list_display=['id','bank_branches']