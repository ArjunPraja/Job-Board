from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Job
from .utils import scrape_jobs
import datetime

def update_jobs():
    last_job = Job.objects.order_by('-posted_on').first()
    
    if not last_job or (datetime.datetime.now().astimezone() - last_job.posted_on).days >= 1:
        jobs_data = scrape_jobs()
        
        if jobs_data:
           
            for job_data in jobs_data:
                Job.objects.get_or_create(
                    title=job_data['title'],
                    company=job_data['company'],
                    defaults=job_data
                )

def job_list(request):
    """View for displaying job listings with search and filter functionality"""
    update_jobs()
    
    query = request.GET.get("search", "")
    location = request.GET.get("location", "")
    experience = request.GET.get("experience", "")
    
    jobs = Job.objects.all().order_by('-posted_on')
    
    if query:
        jobs = jobs.filter(title__icontains=query)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if experience:
        jobs = jobs.filter(experience__icontains=experience)
    
    paginator = Paginator(jobs, 5)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    all_locations = Job.objects.values_list('location', flat=True).distinct()
    all_experiences = Job.objects.values_list('experience', flat=True).distinct()
    
    context = {
        "page_obj": page_obj,
        "query": query,
        "location": location,
        "experience": experience,
        "all_locations": all_locations,
        "all_experiences": all_experiences,
    }
    
    return render(request, "jobs/job_list.html", context)

def job_detail(request, pk):
    """View for displaying detailed information about a job"""
    job = get_object_or_404(Job, pk=pk)
    return render(request, "jobs/job_detail.html", {"job": job})