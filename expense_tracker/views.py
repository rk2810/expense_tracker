from django.shortcuts import render, get_object_or_404
from expense_tracker.models import Transaction, Category



def transaction_list(request):
    transaction = Transaction.objects.all()
    return render(request, 'list.html', {'transactions': transaction})


def transaction_major(request):
    transaction = get_object_or_404(Transaction, amount__gte=1500)
    return render(request, 'list.html', {'transactions': transaction})

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

