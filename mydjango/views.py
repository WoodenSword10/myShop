from django.shortcuts import render

# Create your views here.
def init_view(request):
    return render(request, 'html/mypython/python_init.html')

def python_view(request):
    return render(request, 'html/mypython/python常用库.html')