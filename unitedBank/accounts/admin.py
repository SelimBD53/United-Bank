from django.contrib import admin

# Register your models here.
from models import User, UserBankAccount, UserAddress, BankAccountType

admin.site.register(User)
admin.site.register(UserBankAccount)
admin.site.register(UserAddress)
admin.site.register(BankAccountType)