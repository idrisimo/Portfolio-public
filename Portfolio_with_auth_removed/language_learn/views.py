from django.shortcuts import render

# Create your views here.


def dashboard_view(request):

    context = {}
    return render(request, 'dashboard.html', context)