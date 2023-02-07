from django.shortcuts import render
from .models import Job
# Create your views here.
def job_list(request):
    jobs_list = Job.objects.all()
    context = {'jobs' : jobs_list}
    return render(request , 'jobs.html' ,context)