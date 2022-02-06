from django.shortcuts import render

# Create your views here.
def sklearn_view(request):
    return render(request, 'html/sklearn_use.html')
