# DevOps Portfolio

Hands-on DevOps projects covering the core of the modern workflow: **automate delivery, observe what is running, and provision infrastructure as code.**

Each project lives in its own repository with its own README, setup steps and tear-down instructions.

## Selected Projects

|Project|What it shows|Stack|
|-|-|-|
|[**Django CI/CD Pipeline**](https://github.com/YOUR_GITHUB_USERNAME/django-cicd-pipeline)|A GitHub Actions pipeline that tests, builds a Docker image and deploys on every push|Django, Docker, GitHub Actions, GHCR|
|[**Containerised Monitoring Stack**](https://github.com/YOUR_GITHUB_USERNAME/monitoring-stack)|Prometheus, Grafana and Alertmanager with dashboards and alert rules, run with one command|Prometheus, Grafana, Docker Compose|
|[**Terraform on AWS**](https://github.com/YOUR_GITHUB_USERNAME/terraform-aws-free-tier)|A free-tier EC2 instance, security group and S3 bucket provisioned as code, then destroyed|Terraform, AWS|

\---

## 1\. Django CI/CD Pipeline

A small Django JSON API wired to a full pipeline.

```
push to main ──► test ──► build Docker image ──► push to GHCR ──► deploy over SSH
```

* Tests run on every push and pull request
* Images are tagged `latest` and with the commit SHA
* Deployment is opt-in through a repository variable and secrets, so the pipeline stays green without a server

**Skills:** GitHub Actions, Docker, container registries, automated testing, secrets management.

## 2\. Containerised Monitoring Stack

A Docker Compose lab with a metrics-instrumented Flask app, host metrics, provisioned Grafana dashboards and Prometheus alert rules (instance down, high error rate, high latency, high CPU).

```
app + node-exporter ──► Prometheus ──► Grafana (dashboards)
                            └────────► Alertmanager (alerts)
```

The README maps the setup to Nagios and Splunk concepts: active checks and thresholds become PromQL alert rules, and log dashboards become metric dashboards.

**Skills:** Prometheus, PromQL, Grafana provisioning, Alertmanager, Docker Compose, observability fundamentals.

## 3\. Terraform on AWS

Infrastructure as code for a small, free-tier-friendly environment:

* EC2 instance (Amazon Linux 2023, IMDSv2 enforced, encrypted volume) running nginx in Docker
* Security group with HTTP open and SSH restricted to a single CIDR
* S3 bucket with versioning, encryption and public access blocked

Full lifecycle covered: `init → plan → apply → destroy`.

**Skills:** Terraform, AWS (EC2, VPC security groups, S3), least-privilege networking, cost awareness.

\---

## How the projects connect

The Terraform project can create the server that the CI/CD pipeline deploys to, and the monitoring stack shows how you would observe that application in production.

## Tools

!\[Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker\&logoColor=white)
!\[GitHub Actions](https://img.shields.io/badge/GitHub\_Actions-2088FF?logo=githubactions\&logoColor=white)
!\[Terraform](https://img.shields.io/badge/Terraform-7B42BC?logo=terraform\&logoColor=white)
!\[AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazonwebservices\&logoColor=white)
!\[Prometheus](https://img.shields.io/badge/Prometheus-E6522C?logo=prometheus\&logoColor=white)
!\[Grafana](https://img.shields.io/badge/Grafana-F46800?logo=grafana\&logoColor=white)
!\[Django](https://img.shields.io/badge/Django-092E20?logo=django\&logoColor=white)

## 

