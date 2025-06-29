## A duplicate of the ALX Travel App

---

### ✅ Phase 1: Database Modeling and Data Seeding in Django

**Objective:**  
Define the database models, create serializers for API data representation, and implement a management command to seed the database.

---

#### 📝 Instructions

##### 🔁 Duplicate Project

```bash
cp -r alx_travel_app alx_travel_app_0x00
# implement seeders 
python manage.py seed
```

###  Phase 2: Chapa Payment Integration
**Objective:**
Integrate the Chapa API for secure online payments tied to user bookings.
create the models and views in the listings app

### ✅ Phase 3: Celery Setup (with Redis on Windows via WSL)
🛠 Install Requirements
``` bash
pip install celery redis
```

### ✅ Running Redis on Windows via WSL
🐧 Step 1: Open Ubuntu (WSL)
```bash
sudo apt update
sudo apt install redis-server
# ▶️ Step 2: Start Redis
sudo service redis-server start
# 🧪 Step 3: Test Redis
redis-cli ping
# PONG
```