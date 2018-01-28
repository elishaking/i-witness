from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html', {'first_name': 'King', 'last_name': 'Elisha'})


def profile(request):
    return render(request, 'profile.html', {'first_name': 'King', 'last_name': 'Elisha'})


def reports(request):

    return render(request, 'reports.html', {'first_name': 'King', 'last_name': 'Elisha'})
