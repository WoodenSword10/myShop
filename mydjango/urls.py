from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_view),
    path('uulib/', views.python_view)
]