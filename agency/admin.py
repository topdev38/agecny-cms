  
from django.contrib import admin
from .models import Subscriber, Contact, Team_member, Customer

@admin.register(Subscriber, Contact, Team_member, Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass