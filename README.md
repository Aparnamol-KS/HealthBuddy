# HealthBuddy🩺

HealthBuddy is a health-focused web application built using Django that integrates the **IBM Watson chatbot** to provide users with intelligent, interactive health-related assistance and answers to their queries. The project also features a user-friendly web interface to interact with the chatbot seamlessly.

---

## Features

- ***IBM Watson Chatbot Integration** for natural language health queries*  
- *Interactive chatbot interface embedded in the web application*  
- *Modular Django-based architecture*  
- *Provides reliable health-related information and guidance through AI-powered conversations*  

---

## Tech Stack

- Python 3.x  
- Django Web Framework  
- IBM Watson Assistant (chatbot service)  
- SQLite (default Django database)  
- HTML, CSS, JavaScript for frontend  
- Vercel (deployment)  

---

## Getting Started

### Prerequisites

- Python 3.8 or higher  
- Git  
- IBM Cloud account with Watson Assistant service set up  
- (Optional) Virtual environment tool like `venv` or `virtualenv`  

### Installation

#### 1. Clone the repository

   ```
   git clone https://github.com/Aparnamol-KS/HealthBuddy.git
   cd HealthBuddy
  ```
#### 2. Create and activate a virtual environment (recommended)
```
python -m venv env
source env/bin/activate       # On Windows: env\Scripts\activate
```
#### 3. Install the dependencies
```
pip install -r requirements.txt
```
#### 4. Configure IBM Watson Assistant credentials (API key, URL, Assistant ID) in your Django settings or environment variables.

#### 5. Apply database migrations
```
python manage.py migrate
```

#### 6. Run the development server
```
python manage.py runserver
```

## Deployment
This project can be deployed on platforms like Vercel or any hosting service supporting Python and Django.
