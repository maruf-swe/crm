from django.shortcuts import render


def home(request):
    return render(request, 'accounts/products.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')