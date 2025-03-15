import http.client
import json

def scrape_jobs():
    """
    Fetch job listings from the LinkedIn Job Search API.
    """
    conn = http.client.HTTPSConnection("linkedin-job-search-api.p.rapidapi.com")

    
    headers = {
        'x-rapidapi-key': "f5bc5f96d7msh9ba0737754536a4p17b790jsn00c81579bedf",
        'x-rapidapi-host': "linkedin-jobs-api2.p.rapidapi.com"
    }



    try:
        conn.request("GET", "/active-jb-24h", headers=headers)
        res = conn.getresponse()
        
        if res.status != 200:
            print(f"Error: Received status code {res.status}")
            return []

        data = res.read().decode("utf-8")
        job_listings = json.loads(data)
        jobs = []

        if isinstance(job_listings, list):  # Ensure data is iterable
            for job in job_listings:
                experience = job.get("experience", "").strip()
                if not experience:
                    experience = "Experience not specified, but freshers can apply."

                jobs.append({
                    "title": job.get("title", "Not specified"),
                    "company": job.get("organization", "Not specified"),
                    "location": ", ".join(job.get("locations_derived", ["Not specified"])),
                    "experience": experience,
                    "link": job.get("url", ""),
                    "posted_on": job.get("date_posted", "Recent")
                })

        return jobs
    
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON response.")
        return []
    except Exception as e:
        print(f"Error fetching job data: {e}")
        return []
    finally:
        conn.close()

