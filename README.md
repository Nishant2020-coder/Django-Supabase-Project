# Django-Supabase-Project

# Django Supabase Vercel Project

This is a full-stack, serverless web application built with Python (Django) and a PostgreSQL database (Supabase). It's configured for one-click deployment to Vercel.

This project demonstrates:
* **Backend:** Django
* **Database:** Supabase (PostgreSQL)
* **REST API (CRUD):** Django REST Framework for full Create, Read, Update, Delete.
* **3rd-Party API Integration:** A view to fetch data from an external API (JSONPlaceholder).
* **Data Visualization:** A simple report page using Chart.js.
* **Deployment:** Serverless deployment on Vercel.

---

## How to Set Up and Run Locally

### 1. Prerequisites
* Python 3.9+
* A Supabase account (or any public PostgreSQL database).

### 2. Set up Supabase
1.  Go to [supabase.com](https://supabase.com) and create a new project.
2.  Go to **Project Settings** > **Database**.
3.  Find the **Connection string** (select the "URI" tab) and copy your credentials.

### 3. Set up the Local Environment
1.  **Clone this repository:**
    ```bash
    git clone [YOUR_GITHUB_REPOSITORY_URL]
    cd [YOUR_PROJECT_DIRECTORY]
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a `.env` file in the project root. Copy the contents of `.env.example` and fill in your Supabase credentials.

    ```.env
    # .env file
    DB_NAME='postgres'
    DB_USER='postgres'
    DB_PASSWORD='[YOUR-SUPABASE-PASSWORD]'
    DB_HOST='[YOUR-SUPABASE-HOST]'
    DB_PORT='5432'
    SECRET_KEY='[YOUR-DJANGO-SECRET-KEY]' 
    ```
    *You can generate a `SECRET_KEY` using an online tool.*

5.  **Run Migrations:**
    This applies the database schema to your Supabase instance.
    ```bash
    python manage.py migrate
    ```

6.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```
    Your application is now running at `http://127.0.0.1:8000/`.

---

## Project Endpoints

* **Homepage & Report:** `http://127.0.0.1:8000/`
    * This shows the "Article Report" visualization.

* **Fetch External Data:** `http://127.0.0.1:8000/fetch-articles/`
    * Visit this URL to pull 10 posts from JSONPlaceholder and save them to your database. This will populate your report.

* **REST API (CRUD):** `http://127.0.0.1:8000/api/`
    * **List & Create:** `GET /api/articles/`, `POST /api/articles/`
    * **Detail, Update, Delete:** `GET /api/articles/{id}/`, `PUT /api/articles/{id}/`, `DELETE /api/articles/{id}/`
