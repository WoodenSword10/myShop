from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_FPGA_view),
    path('introduce/', views.FPGA_introduce_view),
    path('expore/', views.FPGA_expore_view),
    path('yj/', views.FPGA_yj_view),
    path('zh/', views.FPGA_ZH_view),
    path('mbjg/', views.FPGA_MBJG_view),
    path('xhlx/', views.FPGA_XHLX_view),
    path('cxyj/', views.FPGA_CXYJ_view),
    path('szjz/', views.FPGA_SZJZ_view),
    path('ssysf/', views.FPGE_SSYSF_view),
    path('ljysf/', views.FPGA_LJYSF_view),
    path('gxysf/', views.FPGA_GXYSF_view),
    path('ywysf/', views.FPGA_YWYSF_view),
    path('tjysf/', views.FPGA_TJYSF_view),
    path('pjysf/', views.FPGA_PJYSF_view),
    path('sxlj/', views.FPGA_SXLJ_view),
    path('dcfq/', views.FPGA_DCFQ_view),
    path('sz/', views.FPGA_SZ_view),
    path('sxljdmhyj/', views.FPGA_SXLJDMHYJ_view),
    path('zsfz/', views.FPGA_ZSFZ_view),
]