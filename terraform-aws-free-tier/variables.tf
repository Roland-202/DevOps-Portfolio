variable "region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-1"
}

variable "instance_type" {
  description = "Free-tier eligible type (t2.micro or t3.micro depending on region)"
  type        = string
  default     = "t3.micro"
}

variable "ssh_cidr" {
  description = "CIDR allowed to SSH, e.g. 203.0.113.4/32. Use your own IP, never 0.0.0.0/0"
  type        = string
}

variable "key_name" {
  description = "Existing EC2 key pair name (optional)"
  type        = string
  default     = null
}

variable "project" {
  type    = string
  default = "tf-free-tier-demo"
}
