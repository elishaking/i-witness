from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html', {'first_name': 'King', 'last_name': 'Elisha'})
