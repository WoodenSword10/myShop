from django.shortcuts import render

# Create your views here.
def init_FPGA_view(request):
    return render(request, 'html/FPGA/FPGA_init.html')