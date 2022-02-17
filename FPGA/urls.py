from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_FPGA_view),
    path('introduce/', views.FPGA_introduce_view),
    path('expore/', views.FPGA_expore_view),
    path('yj/', views.FPGA_yj_view),
]