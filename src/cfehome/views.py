from django.shortcuts import render

from visits.models import PageVisit

def home_page_view(request):
    queryset = PageVisit.objects.all()

    context = {
        'queryset': queryset,
        'page_visits_count': queryset.count(),
    }

    PageVisit.objects.create()
    return render(request, 'home.html', context)