from django.urls import path,include
from . import  views

# when I use namespace in: path('jobs/', include('job.urls',namespace='jobs')), in url original "of project"
#we must add: app_name='job'  in url of job

urlpatterns = [
   
    path('', views.job_list,name='job_list'),
    path('add', views.add_job,name='add_job'),
    path('<str:slug>', views.job_detail,name='job_detail'),
]
