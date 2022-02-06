from django.urls import path
from . import views

urlpatterns = [
    path('sklearn/', views.sklearn_view),
]