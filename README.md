## Django Backend Project
- This project is a backend Community application built with Django and Django REST framework, providing APIs for user authentication, community management, and real-time encrypted messaging.

## Table of Contents
- [Features](#features)
- [Apis](#apis)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributions](#contributions)


## Features
- User registration and authentication using JWT.
- CRUD operations for communities and messages.
- Role-based access control for admin and members.
- End-to-end encrypted messaging using Signal Protocol.
- RESTful API endpoints for all functionalities.


## Apis
#### Documentation
You can visit the official Postman documentation here [Api-postman-documentation](https://).



## Requirements
- Python 3.9 or higher
- Django 3.2 or higher
- Django REST Framework 3.12 or higher
- Django Channels 3.0+
- SQLite (default database)


## Installation
1. **Clone the repository:**
   ```bash 
   git clone https://github.com/HenrietteDaughtyOloo/Community_Project.git
   cd Community_Project


## Create a virtual environment:
2. **Create venv:**
   ```bash
   python -m venv myenv
3. **Then activate it:**
   ```bash
   source myenv/bin/activate 
## On Windows, use:
3. **For windows:**
   ```bash
   myenv\Scripts\activate


## Install dependencies:
4. **Then requirements:**
   ```bash
   pip install -r requirements.txt

## Apply migrations:
5. **Migrations:**
   ```bash
   python manage.py migrate

## Run the development server:
6. **Runserver:**
   ```bash
   python manage.py runserver

## Usage
7. **Access API Endpoints:**
#### Remember to create appropriate authorization Headers to use the API
- List of all communities: GET /api/communities/
- Register a user: POST /api/users/register/
- List all messages: GET /api/usermessages/

## Contributions:
9. **To be a contributor:**
Fork the repository:
- Click the "Fork" button at the top right of this repository.

- Clone your fork:
   ```bash
   git clone https://github.com/HenrietteDaughtyOloo/Community_Project.git

- navigate to repository
   ```bash
   cd Community_Project
- Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name

- Make your changes and commit:
   ```bash
   git commit -am 'Add a feature'
- Push to the branch:
   ```bash
   git push origin feature/your-feature-name

- Create a Pull Request:
Go to the repository on GitHub and click the "New Pull Request" button.