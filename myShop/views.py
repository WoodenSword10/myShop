from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def init_html_view(request):
    username = ''
    if request.session.get('username'):
        username = request.session['username']
        return render(request, 'html/init_html.html', locals())
    else:
        return render(request, 'html/init_html.html', locals())
