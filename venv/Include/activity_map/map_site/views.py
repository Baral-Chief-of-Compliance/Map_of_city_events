from django.shortcuts import render

# Create your views here.

def statistics(request):
    return render(request, 'map_site/statistics.html')