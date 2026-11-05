# Django CI/CD Pipeline

A small Django JSON API with a complete GitHub Actions pipeline: **test → build Docker image → deploy**, triggered on every push to `main`.

## Pipeline

| Stage | What it does |
|-------|--------------|
| `test` | Installs deps, runs `manage.py check` and the Django test suite (also runs on pull requests) |
| `build` | Builds the Docker image with Buildx and pushes it to GitHub Container Registry (`ghcr.io`), tagged `latest` and with the commit SHA |
| `deploy` | SSHes into a server, pulls the new image and restarts the container |

The deploy job is opt-in so the pipeline stays green without a server. To enable it, set the repo variable `DEPLOY_ENABLED=true` and add the secrets `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_SSH_KEY` and `DJANGO_SECRET_KEY`. A free-tier EC2 instance with Docker installed works well (see my Terraform project).

## Endpoints

- `GET /health/` – health check
- `GET /tasks/` – list tasks
- `POST /tasks/` – create a task, body `{"title": "..."}`

## Run locally

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py test
python manage.py runserver
```

Or with Docker:

```bash
docker build -t django-cicd .
docker run -p 8000:8000 django-cicd
```

## Skills demonstrated
GitHub Actions, Docker, container registries, automated testing, SSH-based deployment, secrets management.
