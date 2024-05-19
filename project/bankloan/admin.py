from django.contrib import admin
from .models import User,customer_detail,payment

admin.site.register(User)
admin.site.register(customer_detail)
admin.site.register(payment)