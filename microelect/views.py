from django.shortcuts import render

# Create your views here.

def init_view(request):
    return render(request, 'html/micro_init.html')
