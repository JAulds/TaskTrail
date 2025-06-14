# 🧩 TaskTrail

TaskTrail is a lightweight, full-stack task and project management tool designed for small teams, startups, and NGOs. Built using React, Django REST Framework, PostgreSQL, Redis, and Docker — it enables secure role-based task collaboration with modern DevOps support.

---

## 🚀 Features

- 🔐 **JWT Authentication** with roles: `admin`, `member`
- 📁 Create & manage **projects and tasks**
- ✅ **Status updates** and assignments
- 🧑‍🤝‍🧑 Role-based access control
- ⚙️ Dockerized backend + frontend + database + Redis
- 🧠 Redis caching for homepage/project/task data
- 🐛 Structured logging for backend
- 🧪 Unit and E2E testing support

---

## 🛠️ Tech Stack

| Layer       | Stack                         |
|-------------|-------------------------------|
| Frontend    | React, Axios, React Router    |
| Backend     | Django REST Framework         |
| Database    | PostgreSQL                    |
| Caching     | Redis                         |
| Container   | Docker, docker-compose        |
| Web server  | Nginx                         |
| Auth        | JWT via SimpleJWT             |
| Testing     | Django TestCase               |

---

## ⚙️ Local Development Setup

> Ensure you have Docker + Docker Compose installed.

```bash
# Clone the repository
cd tasktrail

# Install dependencies
pip install -r requirement.txt

# Start server
python manage.py runserver

# --------- Other Features ---------

# Add superuser/admin
python manage.py createsuperuser

# Run tests
python manage.py test TrailApp

# Access admin page
# Add /admin to end of base url to access and login to admin page to add tasks
# Anyone who has an account can mark the status of the task by using the website (Not Started, In Progress, Completed)
# Tasks are sorted by closest due date and grouped by the week they are due

