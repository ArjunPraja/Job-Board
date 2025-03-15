from django.core.management.base import BaseCommand
from jobs.utils import scrape_jobs
from jobs.models import Job

class Command(BaseCommand):
    help = 'Scrape jobs from job portals and save to database'

    def handle(self, *args, **options):
        self.stdout.write('Starting job scraping...')
        
        jobs_data = scrape_jobs()
        print(jobs_data)
        if not jobs_data:
            self.stdout.write(self.style.WARNING('No jobs found or error occurred during scraping.'))
            return
            
        new_jobs = 0
        for job_data in jobs_data:
            job, created = Job.objects.get_or_create(
                title=job_data['title'],
                company=job_data['company'],
                defaults=job_data
            )
            if created:
                new_jobs += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Job scraping completed. Added {new_jobs} new jobs out of {len(jobs_data)} scraped.')
        )