from django.shortcuts import render

# Create your views here.
def sklearn_view(request):
    return render(request, 'html/myML/sklearn_use.html')
