from django.shortcuts import render

from visits.models import PageVisit

def home_view(request):
    return about_view(request)

def about_view(request):
    qs = PageVisit.objects.all()

    context = {
        'qs': qs,
        'page_visits_count': qs.count(),
    }

    PageVisit.objects.create()
    return render(request, 'home.html', context)