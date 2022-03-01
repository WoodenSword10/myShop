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

def FPGA_ZH_view(request):
    return render(request, 'html/FPGA/综合和仿真.html')

def FPGA_MBJG_view(request):
    return render(request, 'html/FPGA/模板结构.html')

def FPGA_XHLX_view(request):
    return render(request, 'html/FPGA/信号类型.html')

def FPGA_CXYJ_view(request):
    return render(request, 'html/FPGA/程序语句.html')

def FPGA_SZJZ_view(request):
    return render(request, 'html/FPGA/数字进制.html')

def FPGE_SSYSF_view(request):
    return render(request, 'html/FPGA/算术运算符.html')

def FPGA_LJYSF_view(request):
    return render(request, 'html/FPGA/逻辑运算符.html')

def FPGA_GXYSF_view(request):
    return render(request, 'html/FPGA/关系运算符.html')

def FPGA_YWYSF_view(request):
    return render(request, 'html/FPGA/移位运算符.html')

def FPGA_TJYSF_view(request):
    return render(request, 'html/FPGA/条件运算符.html')

def FPGA_PJYSF_view(request):
    return render(request, 'html/FPGA/拼接运算符.html')

def FPGA_SXLJ_view(request):
    return render(request, 'html/FPGA/时序逻辑.html')

def FPGA_DCFQ_view(request):
    return render(request, 'html/FPGA/D触发器.html')

def FPGA_SZ_view(request):
    return render(request, 'html/FPGA/时钟.html')

def FPGA_SXLJDMHYJ_view(request):
    return render(request, 'html/FPGA/时序逻辑代码和硬件.html')

def FPGA_ZSFZ_view(request):
    return render(request, 'html/FPGA/阻塞赋值和非阻塞赋值.html')