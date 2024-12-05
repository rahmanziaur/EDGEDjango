# EDGEDjango

EDGEDjango is a Django-based web application designed for Machine Learning Model Serving. It allows users to upload datasets, build machine learning models, and make predictions using those models. The application leverages Django's built-in authentication system for secure login, logout, and registration.

---
## Folder Structure

The project follows a standard Django application structure with the following organization:

```
EDGEDjango/
│
├── App_build/        # Handles dataset upload and model building
├── App_login/        # Handles user authentication
├── App_predict/      # Handles model prediction
├── db.sqlite3
├── EDGEDjango/
    ├── settings.py
    ├── urls.py
    ├── views.py
├── manage.py         # Django management script
├── media/            # all uploaded files
├── static/           # Static files (CSS, JS, Images)
├── templates/        # HTML templates for the application
└── requirements.txt  # List of dependencies
```

# Features

- **User Authentication**: Built-in Django authentication for login, logout, and user registration.
- **Dataset Upload**: Users can upload CSV files containing machine learning data.
- **Model Building**: Users can build machine learning models (e.g., Random Forest Classifier) using the uploaded datasets. The application currently uses the **Iris dataset** as an example.
- **Model Evaluation**: Displays performance metrics like accuracy and F1-score for the built model.
- **Prediction**: Users can select a pre-built model, input new data (e.g., sepal length, petal length, etc.), and classify the Iris dataset.

---

## Applications Overview

### 1. **App_login**
Handles user authentication features:
- User login
- User logout
- User registration

### 2. **App_build**
Allows users to:
- Upload datasets (CSV format)
- View the list of uploaded datasets
- Build a machine learning model (Random Forest Classifier for the Iris dataset)
- View model details (accuracy, F1-score, etc.)

### 3. **App_predict**
Allows users to:
- Select a previously built model
- Input new data for prediction
- Predict and classify data using the built model

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- Django 4.2+
- Required Python packages (listed in `requirements.txt`)

### Installation
**1. Clone the repository:**
   git clone https://github.com/rahmanziaur/EDGEDjango
   
**3. Navigate to the project directory:**
   cd EDGEDjango
   
**4. Install dependencies:**
   pip3 install -r requirements.txt

**5. Run migrations:**
   python3 manage.py makemigrations
   
   python3 manage.py migrate

**6. Start the development server:**
   python3 manage.py runserver
   
**7.** Open the application in browser at http://127.0.0.1:8000.

Videos on this project (Step by step):
https://youtube.com/playlist?list=PL1i5urQUb6bh9xtCNhGLyJBCTmP-sEnLG&si=cjCcDW5cE-MwbT6Y
