# TaskTrail

TaskTrail is a lightweight, full-stack task and project management tool designed for small teams, startups, and NGOs. Built using React, Django REST Framework, PostgreSQL, Redis, and Docker. It enables secure role-based task collaboration with modern DevOps support.

---

## Features

- **Django Authentication** with roles: `admin`, `member`
- Create & manage **projects and tasks**
- **Status updates** and assignments
- Role-based access control
- Dockerized backend + frontend + database
- Memcached caching for homepage/project/task data
- Structured logging for backend
- Unit and E2E testing support

---

## Tech Stack

| Layer       | Stack                         |
|-------------|-------------------------------|
| Frontend    | Django, HTML                  |
| Backend     | Django REST Framework         |
| Database    | SQLite, PostgreSQL            |
| Caching     | Memcached, Dummy              |
| Container   | Docker, docker-compose        |
| Web server  | Nginx, Gunicorn               |
| Auth        | Django Authentication         |
| Testing     | Django TestCase               |

---

## Local Development Setup

> Ensure you have Docker + Docker Compose installed.

```bash
# Clone the repository and change directory
cd tasktrail

# Run docker-compose
docker-compose up -d

# Go to the website
http://localhost:8000/

# --------- Other Features ---------

# Add superuser/admin for local
python manage.py createsuperuser

# Run tests local
python manage.py test TrailApp

# Access admin page
# Add /admin to end of base url to access and login to admin page to add tasks
# Anyone who has an account can mark the status of the task by using the website (Not Started, In Progress, Completed)
# Tasks are sorted by closest due date and grouped by the week they are due
