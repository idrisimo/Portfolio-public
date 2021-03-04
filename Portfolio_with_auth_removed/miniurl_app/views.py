from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from .ProjectScripts.url_shortener import make_miniurl

from .models import *
from .forms import *

def urlshortener_view(request):
    form = Urlcreation_form()
    return_url = request.build_absolute_uri('/miniurl/')
    if request.method == 'POST':
        form = Urlcreation_form(request.POST)
        if form.is_valid():
            urlend = make_miniurl(8)
            instance = form.save(commit=False)
            instance.short_string = urlend
            instance.save()
            messages.success(request, (return_url + urlend))
            return HttpResponseRedirect('/miniurl_shortener/')
    context = {'form':form}
    return render(request, 'miniurl.html', context)

def checkurl(request, urlend):
    urlmodel = Urlmodel.objects.get(short_string=urlend)
    print('redirected')
    return redirect(urlmodel.long_url)