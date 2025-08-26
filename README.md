# Real Time Monitoring Logs (RTML) – Django App

## 📌 Overview
This Django application was created to replace a manual, Excel-based workflow used at my former workplace for logging team actions during the monitoring of call center services.  

Previously, workforce analysts had to:
- Log monitoring actions into daily Excel files.  
- Daily add new excel files for the monitored services.  
- Manage folders for each month’s files.  
- Archive older files and folders.  

This was inefficient and time-consuming.  

The app automates this workflow by:  
- Using a **Django database** to store monitoring comments.  
- Connecting to an **external database** to fetch and display key performance indicators (KPIs).  
- Removing the need to manage multiple Excel files and folders.  

---

## 🚀 Features
- Store monitoring logs in a structured Django database.  
- View and analyze team input in one centralized dashboard.  
- Connect to external databases to automatically fetch KPIs (e.g., service levels, call volumes, forecast).  
- Archive and retrieve historical data without handling files manually.  
- **Role-based access**:  
  - Users in the **WFM group** see an **“Add comment”** button in the navigation bar, allowing them to submit new monitoring entries through an offcanvas form.  
  - Users not in the **WFM group** have **read-only access**, meaning they can view the monitoring table but cannot add new comments.  


---

## ⚙️ Tech Stack
- **Backend:** Django (Python)  
- **Database:** MySQL (with `django-environ` for environment variables)  
- **Frontend:** Django templates + Bootstrap 4  
- **External DB connection:** Multiple databases (`default` and `kpi`)  


## ⚡ Getting Started
1. Clone the repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows

3. Install dependencies
`pip install -r requirements.txt`

4. Configure environment variables

This project uses django-environ to manage secrets and database credentials.
Create a .env file in the project root with the following variables:
```
# Django secret
DJANGO_SECRET_KEY=your_secret_key

# Default Database (App storage)
DEFAULT_DB_NAME=your_db_name
DEFAULT_DB_USER=your_db_user
DEFAULT_DB_PASSWORD=your_db_password
DEFAULT_DB_HOST=localhost
DEFAULT_DB_PORT=3306

# KPI Database (External source)
KPI_DB_NAME=your_kpi_db_name
KPI_DB_USER=your_kpi_db_user
KPI_DB_PASSWORD=your_kpi_db_password
KPI_DB_HOST=external_host
KPI_DB_PORT=3306
```

⚠️ Make sure MySQL is running and both databases are accessible.

5. Run migrations
`python manage.py migrate`

6. Create a superuser
`python manage.py createsuperuser`

7. Collect static files (for production)
`python manage.py collectstatic`

8. Start the development server
`python manage.py runserver`


Visit the app at: http://127.0.0.1:8000/

---

## 📊 Use Cases

Real-time monitoring of call center KPIs.

Logging workforce management actions and decisions.

Replacing messy Excel file management with a centralized, searchable system.

---
