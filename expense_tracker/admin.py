from django.contrib import admin
from expense_tracker.models import Transaction, Currency, Category, Account

# admin.site.register(Transaction)
# admin.site.register(Currency)
# admin.site.register(Category)
# admin.site.register(Account)


@admin.register(Transaction)
class CreateTransaction(admin.ModelAdmin):
    search_fields = ('title', 'category', 'account')
    ordering = ('date_time',)


@admin.register(Currency)
class CreateCurrency(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Category)
class CreateCategory(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Account)
class CreateAccounts(admin.ModelAdmin):
    search_fields = ('name', 'description')
