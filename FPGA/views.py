from django.shortcuts import render

# Create your views here.
def init_FPGA_view(request):
    return render(request, 'html/FPGA/FPGA_init.html')

def FPGA_introduce_view(request):
    return render(request, 'html/FPGA/FPGA介绍.html')

def FPGA_expore_view(request):
    return render(request, 'html/FPGA/FPGA开发流程.html')

def FPGA_yj_view(request):
    return render(request, 'html/FPGA/硬件描述语言.html')