## ALX Travel App 0x01

## ✈️ Overview

This project is an API for managing **travel listings and bookings**, built using Django and Django REST Framework. It provides full CRUD functionality and comes with auto-generated API documentation using Swagger (via `drf-yasg`).

---

## 📁 Project Structure


##### step 1: Create Django Project and App
Open your terminal and run:

Duplicate the project `alx_travel_app_0x00` to `alx_travel_app_0x01`

**Create a Python virtual environment**
`python3 -m venv venv`
`source venv/bin/activate  # On Windows: venv\Scripts\activate`
`pip install -r requirements.txt`

**Create the listings app**
`python manage.py startapp listings`

**create seed**
`python manage.py seed`

Create an app within the project named listings.
Install necessary packages, including django, djangorestframework, django-cors- headers, celery, rabbitmq, and drf-yasg for Swagger documentation.

create a .env file

Configure Settings:

In settings.py, configure the project for REST framework and CORS headers.
Set up the database configuration to use MYSQL. Use environment variables for sensitive information such as database credentials. (Hint: Use the django-environ package to handle .env files).
Add Swagger:

Install drf-yasg for Swagger documentation.
Configure Swagger to automatically document all APIs. The documentation should be available at /swagger/.
Initialize Git Repository:

Initialize a Git repository and make your initial commit with the project setup files.