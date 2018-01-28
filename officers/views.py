from django.shortcuts import render

from reports.models import Report


# Create your views here.
def dashboard(request):
    resolved_reports = Report.objects.filter(resolved=False)
    context = {
        'first_name': 'King',
        'last_name': 'Elisha',
        'reports': resolved_reports,
        'a1': 'active'
    }
    return render(request, 'dashboard.html', context)


def profile(request):
    return render(request, 'profile.html', {'first_name': 'King', 'last_name': 'Elisha', 'a2': 'active'})


def reports(request):
    unresolved_reports = Report.objects.filter(resolved=False)
    resolved_reports = Report.objects.filter(resolved=True)
    context = {
        'first_name': 'King',
        'last_name': 'Elisha',
        'reports': unresolved_reports,
        'resolved_reports': resolved_reports,
        'a3': 'active'
    }
    return render(request, 'reports.html', context)
