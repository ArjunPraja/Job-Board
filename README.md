# **Django Job Board - Automated Job Listings**

A **dynamic and automated job board** built with **Django** that fetches job listings from **RapidAPI** every 24 hours. Users can **filter jobs** based on **title, location, and experience**, and apply directly by redirecting to the job source.  

🔗 **Live Demo**: [Job Board on PythonAnywhere](https://arjunprajapati2801.pythonanywhere.com/)

---

## **🛠 Features**
✅ Fetches **real-time job data** from RapidAPI  
✅ **Auto-updates** job listings every 24 hours  
✅ **Filter** jobs by **title, location, and experience**  
✅ **Apply directly** by redirecting to the job posting  
✅ Deployed on **PythonAnywhere**  

---

## **⚙️ Tech Stack**
- **Backend:** Django  
- **Frontend:** HTML, CSS, JavaScript, Tailwind CSS  
- **Database:** SQLite  
- **API Integration:** RapidAPI (Job Listings API)  
- **Hosting:** PythonAnywhere  
- **Automation:** Cron Job (Auto-fetch data every 24 hours)  

---

## **🚀 Installation & Setup**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/ArjunPraja/Job-Board.git
cd Job-Board
```

### **2️⃣ Create & Activate a Virtual Environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a **.env** file in the root directory and add:  
```bash
RAPIDAPI_KEY=your_api_key
```

### **5️⃣ Apply Migrations & Run Server**
```bash
python manage.py migrate
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` to see the job board locally. 🎉  

---

## **🔗 API Integration (RapidAPI)**
This job board uses **RapidAPI** to fetch job listings.  
**API Used:** LinkedIn Jobs API  
**Endpoint:** `/active-jb-24h`

### **How Data is Fetched?**
- A **Django management command** fetches job data and updates the database.
- A **cron job** runs every 24 hours on **PythonAnywhere** to keep job listings fresh.

#### **API Request Example:**
```python
import http.client

conn = http.client.HTTPSConnection("linkedin-job-search-api.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "your_api_key",
    'x-rapidapi-host': "linkedin-job-search-api.p.rapidapi.com"
}

conn.request("GET", "/active-jb-24h", headers=headers)
```

---

## **🛠 Automated Data Fetching (Cron Job)**
A scheduled cron job updates job listings **every 24 hours** using:
```bash
python manage.py scrape_jobs
```
This ensures users always see **the latest jobs** without manual updates.  

---

## **📞 Contact**
👨‍💻 **Arjun Vishnubhai Prajapati**  
📞 **+91 8128781062**
📧 **[Email](prajapatiarjun2801@gmail.com)**  
🔗 **[LinkedIn](https://www.linkedin.com/in/prajapati-arjun-42310b268/)**

