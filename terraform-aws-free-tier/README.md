# Terraform on AWS: Free-Tier Setup

Infrastructure as code that provisions a small, free-tier-friendly environment:

- **EC2** instance (Amazon Linux 2023, latest AMI via SSM, IMDSv2 enforced, encrypted root volume) running nginx in Docker
- **Security group**: HTTP open, SSH restricted to one CIDR
- **S3 bucket**: unique name, versioning, SSE encryption, all public access blocked

## Usage

```bash
aws configure                                  # or export AWS_PROFILE
cp terraform.tfvars.example terraform.tfvars   # set ssh_cidr to your IP
terraform init
terraform plan
terraform apply
```

Open the `web_url` output in a browser.

## Tear down (avoid charges)

```bash
terraform destroy
```

## Cost notes
Designed to stay inside the AWS Free Tier for new accounts (750 hrs/month of a micro instance, 5 GB S3). Always destroy when done and check the Billing dashboard. Confirm which micro type is free-tier eligible in your region and adjust `instance_type`.

## Concepts demonstrated
Providers and data sources, variables and outputs, resource dependencies, least-privilege security groups, S3 hardening, and the full lifecycle (`init → plan → apply → destroy`).

## Next steps
Remote state in S3 with DynamoDB locking, split into modules, and run `terraform fmt` / `validate` in a GitHub Actions pipeline like my Django project.
