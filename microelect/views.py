from django.shortcuts import render

# Create your views here.

def init_view(request):
    return render(request, 'html/mircoelect/micro_init.html')
