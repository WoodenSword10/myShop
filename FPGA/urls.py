from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_FPGA_view),
]