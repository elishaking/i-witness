from django.shortcuts import render

# from geopy.geocoders import Nominatim

from reports.models import Report


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html', {'first_name': 'King', 'last_name': 'Elisha'})


def profile(request):
    return render(request, 'profile.html', {'first_name': 'King', 'last_name': 'Elisha'})


def reports(request):
    unresolved_reports = Report.objects.filter(resolved=False)
    # loc = str(unresolved_reports[len(unresolved_reports) - 1].location).split(',')
    # unresolved_reports[len(unresolved_reports) - 1].location = str(Nominatim().reverse('{0}, {1}'.format(loc[0], loc[1])))
    resolved_reports = Report.objects.filter(resolved=True)
    context = {
        'first_name': 'King',
        'last_name': 'Elisha',
        'reports': unresolved_reports,
        'resolved_reports': resolved_reports
    }
    return render(request, 'reports.html', context)
