from django import forms
from .models import Transaction, Budget

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['user', 'category', 'amount', 'date', 'description']  

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = [ 'category', 'limit']  
