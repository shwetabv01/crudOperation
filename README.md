# Full Stack Developer Demo - Django + PostgreSQL

This is a demo web application built using **Python (Django)** with **PostgreSQL**.  
The app demonstrates:
1. **CRUD operations** via REST APIs  
2. **Integration with a third-party API** (RandomUser API)  
3. **Simple data visualization** (patient age distribution chart)  

---

## 🚀 Features

- **Patient Management**
  - Add, view, update, delete patients
  - 7+ fields in the database (first name, last name, age, gender, email, phone, address, created_at)
- **Third-party API Integration**
  - Fetch random patient data from `https://randomuser.me/api/`
- **Visualization**
  - Histogram of patient ages generated with matplotlib

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone "https://github.com/shweta/fullstack-demo.git"
cd fullstack-demo

### 2. Create Virtual Environment
python -m venv venv
# Activate it
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Configure Database
Update crud_demo/settings.py with your PostgreSQL credentials:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'demo_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres@123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Create the database in PostgreSQL:
CREATE DATABASE demo_db;

5. Run Migrations
python manage.py makemigrations
python manage.py migrate

6. Create Superuser (Optional)
python manage.py createsuperuser

7. Start Server
python manage.py runserver


🧪 Testing the Application
CRUD APIs
List patients → GET http://127.0.0.1:8000/api/patients/
Create patient → POST http://127.0.0.1:8000/api/patients/
Retrieve patient → GET http://127.0.0.1:8000/api/patients/<id>/
Update patient → PUT http://127.0.0.1:8000/api/patients/<id>/
Delete patient → DELETE http://127.0.0.1:8000/api/patients/<id>/

Third-party API Integration
Add random patient (from RandomUser API)
POST http://127.0.0.1:8000/api/add-random/

Visualization
Patient age distribution
GET http://127.0.0.1:8000/api/age-chart/


