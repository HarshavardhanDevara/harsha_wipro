# Capstone Project Customer Relationship Management (CRM) System
## Flask CRM Web Application

A feature-rich CRM (Customer Relationship Management) web application built using Flask. This application allows users to manage customers, interactions, and reviews efficiently.

## Features
- **Customer Management**: Add, edit, delete, and search customers.
- **Interaction Tracking**: Record and manage interactions with customers.
- **Review System**: Add and view customer reviews with ratings.
- **Dashboard**: Visualize key metrics and monthly interactions using charts.
- **Real-Time Updates**: Interactions are updated dynamically using WebSockets.

## Table of Contents
1. [Software Requirements](#software-requirements)
2. [How to Run the Application](#how-to-run-the-application)
3. [Development Process](#development-process)
4. [CRUD Operations and Testing with Postman](#crud-operations-and-testing-with-postman)
5. [MySQL Connection Setup](#mysql-connection-setup)
6. [Screenshots](#screenshots)

## Software Requirements
- Python 3.7
- Flask 1.1.1
- SQLAlchemy
- pip
- virtualenv

Required Python modules are listed in `requirements.txt`.

## How to Run the Application

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd flask-crm-web-application
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3.7 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Create a MySQL database named `crm_db`.
   - Update the database URI in `application.py` if needed.

5. **Run the Application**:
   ```bash
   python application.py
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://localhost:5000`.

## Development Process

For Ubuntu 18.04:
- Create a Python 3.7 virtual environment:
  ```bash
  sudo apt install python3.7-venv
  python3.7 -m venv venv
  source venv/bin/activate
  ```

- Install Flask and SQLAlchemy:
  ```bash
  pip install Flask flask_sqlalchemy
  ```

- Set up the project structure and database:
  ```bash
  mkdir crm && cd crm

  ```

- Create the main application file:
  ```bash
  touch application.py
  ```

## CRUD Operations and Testing with Postman

The application supports the following CRUD operations for managing customers, interactions, and reviews. You can test these endpoints using Postman.

### Customers
- **Create**:  
  Method: `POST`  
  URL: `http://localhost:5000/api/customers`  
  Body (JSON):
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "1234567890"
  }
  ```

- **Read**:  
  Method: `GET`  
  URL: `http://localhost:5000/api/customers/<id>`

- **Update**:  
  Method: `PUT`  
  URL: `http://localhost:5000/api/customers/<id>`  
  Body (JSON):
  ```json
  {
    "name": "John Smith",
    "email": "john.smith@example.com"
  }
  ```

- **Delete**:  
  Method: `DELETE`  
  URL: `http://localhost:5000/api/customers/<id>`

### Interactions
- **Create**:  
  Method: `POST`  
  URL: `http://localhost:5000/api/interactions`  
  Body (JSON):
  ```json
  {
    "customer_id": 1,
    "interaction_type": "Call",
    "notes": "Discussed project requirements."
  }
  ```

- **Read**:  
  Method: `GET`  
  URL: `http://localhost:5000/api/interactions/<id>`

- **Update**:  
  Method: `PUT`  
  URL: `http://localhost:5000/api/interactions/<id>`  
  Body (JSON):
  ```json
  {
    "interaction_type": "Email",
    "notes": "Followed up with project details."
  }
  ```

- **Delete**:  
  Method: `DELETE`  
  URL: `http://localhost:5000/api/interactions/<id>`

### Reviews
- **Create**:  
  Method: `POST`  
  URL: `http://localhost:5000/api/reviews`  
  Body (JSON):
  ```json
  {
    "customer_id": 1,
    "rating": 5,
    "review": "Excellent service!"
  }
  ```

- **Read**:  
  Method: `GET`  
  URL: `http://localhost:5000/api/reviews/<id>`

- **Update**:  
  Method: `PUT`  
  URL: `http://localhost:5000/api/reviews/<id>`  
  Body (JSON):
  ```json
  {
    "rating": 4,
    "review": "Good service, but room for improvement."
  }
  ```

- **Delete**:  
  Method: `DELETE`  
  URL: `http://localhost:5000/api/reviews/<id>`

## MySQL Connection Setup

To connect the application to a MySQL database:

1. Install MySQL and create a database:
   ```bash
   sudo apt install mysql-server
   mysql -u root -p
   CREATE DATABASE crm_db;
   ```

2. Update the database URI in `application.py`:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/crm_db'
   ```

3. Install the required MySQL driver:
   ```bash
   pip install pymysql
   ```

4. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```


## Screenshots

### Dashboard
![Dashboard](images/Screenshot%20(92).png)
![Dashboard](images/Screenshot%20(91).png)

### Customer Management
![Customer Management](images/Screenshot%20(83).png)
![Customer Management](images/Screenshot%20(84).png)
![Customer Management](images/Screenshot%20(86).png)
![CM](images/Screenshot%20(85).png)

### Interaction Tracking
![Interaction Tracking](images/Screenshot%20(87).png)
![Interaction Tracking](images/Screenshot%20(88).png)
![Interaction Tracking](images/Screenshot%20(92).png)

### Review System
![Review System](images/Screenshot%20(89).png)