# Django Blog Project

## Introduction
This project was created as part of the lesson "Using APIs & Getting Started with Django." The purpose of this lesson was to introduce Django, a powerful Python web framework, and teach the basics of setting up a Django project, creating apps, and working with Git for version control.

## Project Structure
The project is structured as follows:

- `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can use it to start the server, apply migrations, and manage the database, among other things.

- `mysite/`: The main Django project directory containing configuration files.
  - `settings.py`: Configures project settings, including installed apps, middleware, database, and templates.
  - `urls.py`: Defines the URL patterns for the project, linking paths to different views.
  - `wsgi.py`: Used to serve the application in a production environment.
  - `__init__.py`: Makes `mysite` a Python package.

- `polling/`: A Django app created within the project to manage polling functionality.
  - `models.py`: Defines the data models for the app.
  - `views.py`: Contains the views for displaying polls.
  - `urls.py`: Maps URLs specific to the polling app.
  - `templates/`: Directory containing HTML templates for polling views.
  - `__init__.py`: Makes `polling` a Python package.

- `blogging/`: Another Django app created to manage blog posts.
  - `models.py`: Defines data models for blog posts.
  - `views.py`: Contains the views for displaying blog posts.
  - `urls.py`: Maps URLs specific to the blogging app.
  - `templates/`: Directory containing HTML templates for blog views.
  - `__init__.py`: Makes `blogging` a Python package.

- `db.sqlite3`: SQLite database file where data is stored. This file is created automatically after running migrations.

- `.gitignore`: Specifies files and directories that should be ignored by Git, such as environment files, `__pycache__` directories, and the `db.sqlite3` file.

## Setup Instructions
To run this project, you’ll need to follow these steps:

1. **Clone the Repository**
   ```bash
   git clone [your repository link]
   cd django-blog

2. **Install Dependencies Make sure you have Django installed. You can install Django using:**
   ```bash
   pip install django

3. **Apply Migrations Migrations are used to set up the database schema for the project:**
   ```bash
   python manage.py migrate

4. **Run the Development Server Start the Django development server:**
   ```bash
   python manage.py runserver

5. **Access the Application Open a browser and go to http://127.0.0.1:8000/ to view the project.**
