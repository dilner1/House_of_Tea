from django.shortcuts import render


def suppliersView(request):
    """
        This view loads the newsletter signup form
    """
    suppliers = Suppliers.objects.all()
    context = {
        'products':products,
        }

    return render(request, 'suppliers/suppliers.html')

