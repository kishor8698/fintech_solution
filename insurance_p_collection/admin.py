from django.contrib import admin
from .models import Insurance_p_collection

@admin.register(Insurance_p_collection)
class Insurance_p_collectionAdmin(admin.ModelAdmin):
    list_display=["id"]

