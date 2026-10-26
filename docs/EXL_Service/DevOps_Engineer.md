---
company: "EXL Service"
role: "DevOps Engineer"
experience: "5 years"
tags:
  - interview
  - company/exl-service
  - role/devops-engineer
  - topic/kubernetes
  - topic/terraform
  - topic/aws
  - topic/ci-cd
  - topic/git
  - topic/monitoring
  - topic/sre
  - topic/networking
  - topic/security
---

# EXL Service — DevOps Engineer

- You are onboarding a new customer with 5 million+ users. How would you design the complete application architecture as a Solution Architect?
- Explain your complete CI/CD pipeline from code commit to production deployment.
- Explain your Git branching strategy. How do you deploy code from different branches to different environments?
- If Git is already the source of truth, why do we need Argo CD? Why not deploy directly using the CI/CD pipeline with Helm or kubectl?
- Explain the complete request flow when a user accesses <www.ingress.com> until the request reaches the application pod.
- You need to expose an application internally without using a LoadBalancer or NodePort service. How would you do it?
- Pods in different namespaces can communicate. How would you block that communication? Where would you implement the NetworkPolicy?
- Suppose you are implementing a Canary deployment where only 10% of users receive the new version. How would you implement it through your CI/CD pipeline?
- During a Canary deployment, how would you verify that the 10% deployment is healthy? What metrics would you monitor before proceeding to 100%?
- Do you execute Terraform locally or through a CI/CD pipeline? Explain the complete workflow.
- Two engineers are working on the same Terraform code. How do you prevent conflicts and handle Terraform state locking or drift?
- Draw and explain your Terraform repository structure. How do your dev, qa, and prod environments consume shared modules like the VPC module?
- Two VPCs need to communicate, but their CIDR ranges overlap. Transit Gateway is not allowed. What alternative solution would you recommend?
- Have you worked on Disaster Recovery? Explain your DR strategy, including RTO, RPO, failover, and traffic redirection.
- Explain Rolling Update, Blue-Green, and Canary deployment strategies.
- For a mission-critical production application, which deployment strategy would you choose and why?
- Have you worked on Databricks pipelines? Explain your experience with Databricks.
- What do you know about Apache Hadoop and its ecosystem?
- Which AWS EC2 instance types have you used, and why did you choose them?
- Explain the difference between Git Merge and Git Rebase.
- Give a real-world use case of AWS Lambda.
- Where do you store CI/CD secrets such as pipeline credentials?
- Where do you store application configuration and secrets? (ConfigMaps, Kubernetes Secrets, HashiCorp Vault, etc.)
- A developer accidentally commits AWS credentials to Git. What is your complete incident response process?
- What metrics do you monitor using Prometheus?
- What dashboards and alerts have you configured in Grafana?
- What monitoring agents have you installed in your environment?
- How do you perform infrastructure cost optimization using monitoring and observability tools?
