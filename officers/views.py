from django.shortcuts import render

from reports.models import Report
from media.models import Media


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


def report_details(request, pk):
    report = Report.objects.get(pk=pk)
    media_urls = []
    # print(dir(report.media_files))

    for media_file in report.media_files.values():
        # print(media_file)
        media_urls.append(media_file['file'])

    context = {
        'first_name': 'King',
        'last_name': 'Elisha',
        'report': report,
        'media_urls': media_urls,
        'a3': 'active'
    }
    return render(request, 'report_details.html', context)
