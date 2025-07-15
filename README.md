# Flask Contact Manager

**Flask Contact Manager** is a simple web application that demonstrates how to build a full CRUD interface using:

- **Flask** – a lightweight Python microframework  
- **PostgreSQL** – a powerful, open-source RDBMS  
- **psycopg2** – the official PostgreSQL adapter for Python  
- **Jinja2** – templating engine for dynamic HTML  
- **Bootstrap** – responsive UI components  

This Project contains:

1. **Design** a simple `contacts` table in PostgreSQL  
2. **Connect** Flask to your database using `psycopg2` and `RealDictCursor`  
3. **Implement** routes for Create, Read, Update, and Delete operations  
4. **Render** dynamic pages with Jinja2 templates (`index.html`, `add.html`, `edit.html`)  
5. **Style** your interface with Bootstrap (tables, forms, buttons)  
6. **Deploy** locally or open to your LAN by binding to `0.0.0.0`  

---

### Features

- **List all contacts** with pagination-ready layout  
- **Add new contacts** via a clean Bootstrap form  
- **Edit existing contacts** with pre-filled fields  
- **Delete contacts** using secure POST requests  
- **Configuration** centralised in `config.py` for easy environment changes  

---

### Tech Stack

| Component        | Technology               |
|------------------|--------------------------|
| Web Framework    | Flask (Python)           |
| Database Driver  | psycopg2-binary          |
| Database         | PostgreSQL               |
| Templating       | Jinja2                   |
| UI Styling       | Bootstrap 5 (CDN)        |
| Dev Server       | Flask’s built-in server  |

---

### Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/<your-username>/flask-contact-manager.git
   cd flask-contact-manager

2. **Create and activate a virtualenv**  
    ```bash
    python -m venv venv
    venv\Scripts\activate


3. **Install Dependencies**  
    ```bash
    Flask>=2.0.0
    psycopg2-binary>=2.9.0

4. **Configure your Database**  
    Create a PostgreSQL database named contactdb.
    Update config.py with your connection details.

5. **Initialize the schema**  
    ```bash
    CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20)
    );


6. **Run the app**  
    ```bash
    python app.py

