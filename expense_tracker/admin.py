from django.contrib import admin
from expense_tracker.models import Transaction, Currency, Category, Account

# admin.site.register(Transaction)
# admin.site.register(Currency)
# admin.site.register(Category)
# admin.site.register(Account)


@admin.register(Transaction)
class CreateTransaction(admin.ModelAdmin):
    list_display = ('title', 'user', 'amount', 'comment', 'account', 'category', 'currency', 'date_time', 'flag')
    search_fields = ('title', 'category', 'account')
    ordering = ('date_time',)


@admin.register(Currency)
class CreateCurrency(admin.ModelAdmin):
    list_display = ('name', 'symbol')
    search_fields = ('name',)


@admin.register(Category)
class CreateCategory(admin.ModelAdmin):
    list_display = ('name', 'public')
    search_fields = ('name',)


@admin.register(Account)
class CreateAccounts(admin.ModelAdmin):
    list_display = ('name', 'description', 'color')
    search_fields = ('name', 'description', 'color')
