from django.contrib import admin

# Register your models here.
from django.contrib import admin
from transactions.models import Transaction
from .models import Transaction
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_after_transaction', 'transaction_type', 'loan_approved']
    
    def save_model(self, request, obj, form, change):
        if change:  # If this is an update (not a new transaction)
            # Get the original object from database
            original_obj = Transaction.objects.get(pk=obj.pk)
            
            # If loan approval status changed
            if original_obj.loan_approved != obj.loan_approved:
                if obj.loan_approved:  # Loan is being approved
                    obj.account.balance += obj.amount
                else:  # Loan is being unapproved
                    obj.account.balance -= obj.amount
                    
                obj.balance_after_transaction = obj.account.balance
                obj.account.save()
        else:  # New transaction
            # Only add to balance if it's approved
            if obj.loan_approved:
                obj.account.balance += obj.amount
                obj.balance_after_transaction = obj.account.balance
                obj.account.save()
        
        super().save_model(request, obj, form, change)