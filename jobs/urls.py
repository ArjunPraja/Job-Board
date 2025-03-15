from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job-list'),
    path('job/<int:pk>/', views.job_detail, name='job-detail'),
]