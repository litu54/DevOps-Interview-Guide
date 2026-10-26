---
company: "SquareOps"
role: "DevOps Engineer"
tags:
  - interview
  - company/squareops
  - role/devops-engineer
  - topic/kubernetes
  - topic/terraform
  - topic/aws
  - topic/ci-cd
  - topic/jenkins
  - topic/git
  - topic/networking
  - topic/security
  - topic/databases
---

# SquareOps — DevOps Engineer

## 🏗️ Infrastructure & Architecture

- Q1. Explain the infrastructure and application setup of your last project. How is the application hosted?
  - Follow-ups:
    - Where exactly is the frontend hosted?
    - Where is the backend hosted?
    - Where is the database stored?
    - Is everything on AWS or multi-cloud?
    - What part of the infra do you manage personally?
    - What are the microservices doing?
    - Why did you choose this architecture?

## ☁️ AWS Cloud Responsibilities

- Q2. What exactly do you do in AWS Cloud in this project?
  - Follow-ups:
    - Do you manage VPC/subnets/security groups?
    - Do you create EC2/EKS/ECS resources?
    - Do you manage S3 lifecycle policies?
    - Do you handle IAM + RBAC in Kubernetes?
    - Do you participate in cost-optimization?
- Q3. On which compute platform are the applications hosted? (Expected: EKS)
  - Follow-ups:
    - Why EKS over ECS?
    - How do you manage worker nodes?
    - How many replicas do you run?
    - Do you use Cluster Autoscaler / Karpenter?

## ☸️ EKS & Kubernetes

- Q4. Have you created an EKS cluster? Explain the process.
  - Follow-ups:
    - Did you use console, CLI, or Terraform?
    - Which VPC/subnet configuration did you use?
    - How did you configure node groups?
    - How do you bootstrap kubectl access?
- Q5. Have you upgraded an EKS cluster before? How?
  - Follow-ups:
    - What risks come with upgrading?
    - How do you handle node draining?
    - Do deployments get recreated?
    - What checks do you perform post-upgrade?
- Q6. If your teammate also wants access to the same cluster through kubectl, what steps do you follow?
  - Follow-ups:
    - What IAM policy do you attach?
    - What is aws-auth ConfigMap?
    - Where is aws-auth stored?
    - How do you map users and roles?
    - Do you provide RoleBinding or ClusterRoleBinding?
- Q7. In which Kubernetes resource do you map IAM users/roles?
  - → AWS Auth ConfigMap
  - Follow-ups:
    - What sections inside it? (mapUsers, mapRoles)
    - What mistakes can break authentication?

## ⛵ Helm & Application Deployment

- Q8. Have you worked with Helm and Helm Charts?
  - Follow-ups:
    - Why use Helm instead of plain YAML?
    - Show the folder structure of a Helm chart.
    - What is the templates folder?
    - What is values.yaml used for?
    - How do you manage multiple environments?
- Q9. How do you securely inject sensitive data into Helm?
  - Follow-ups:
    - Do you use AWS Secrets Manager?
    - Do you avoid committing secrets in values.yaml?
    - What is Sealed Secrets?
    - What is the purpose of --set and --set-file flags?
- Q10. Can a public Helm chart be customized?
  - Follow-ups:
    - Why is it not recommended to edit the chart directly?
    - How do you update config safely?
    - What happens during chart upgrades?
    - How do you extend a chart with new templates?
- Q11. How do you add extra Kubernetes manifest files to a public Helm chart?
  - Follow-ups:
    - Where do you put extra YAML files?
    - How do you reference new values?
    - Can this break the original chart?

## 💾 Kubernetes Storage

- Q12. How to implement shared storage across multiple pods running on multiple nodes in EKS?
  - Follow-ups:
    - Why EFS over EBS?
    - What is the EFS CSI driver?
    - What are the access modes?
    - How do you mount PVC in deployment?
- Q13. If there is one node but multiple pods, can we use EBS for shared storage?
  - Follow-ups:
    - What access mode does EBS support?
    - Why can't EBS work across multiple nodes?
    - When is EFS mandatory?

## 🧠 Kubernetes Reliability & Troubleshooting

- Q14. What is a Pod Disruption Budget (PDB)?
  - Follow-ups:
    - What is voluntary disruption?
    - What is involuntary disruption?
    - When do we use minAvailable vs maxUnavailable?
- Q15. What is your approach to debug a CrashLoopBackOff?
  - Follow-ups:
    - What logs do you check?
    - How do you check events?
    - How do you inspect liveness/readiness probes?
    - How do you check resource limits?
    - How do you inspect environment variables and config maps?
- Q16. During peak traffic, ingress controller is routing requests slowly. How do you debug it?
  - Follow-ups:
    - Check ingress controller logs?
    - Check CPU/memory usage?
    - Check pod replicas?
    - Do you use autoscaling (HPA)?
    - Load balancer throttling issues?
    - Endpoint misconfigurations?
    - Are readiness probes failing?
    - Is target response latency high?
- Q17. Should we increase ingress controller replicas permanently or dynamically?
  - Follow-ups:
    - Why is static scaling bad?
    - When to use HPA?
    - When to use Cluster Autoscaler?

## ☁️ AWS & Cloud Concepts

- Q18. Why choose EFS over EBS?
  - Follow-ups:
    - Which one supports multi-node?
    - Which one is cheaper?
    - Which one is faster?
- Q19. Can EBS be attached to multiple nodes? Why not?
  - Follow-ups:
    - Explain RWO vs RWX
    - Who enforces the mount restriction?

## 🔄 CI/CD

- Q20. What CI/CD tools have you worked with?
  - Follow-ups:
    - Explain your GitHub Actions pipeline.
    - How do you run iOS build automation?
    - How do you handle secrets in pipelines?
    - How do you deploy to EKS through GitHub Actions?
- Q21. How do you handle multi-environment pipelines?
  - Follow-ups:
    - Dev → QA → Prod
    - Promotion strategy (manual approvals?)
    - Git branching strategy?
- Q22. How do you implement rolling deployments?
  - Follow-ups:
    - What happens to old pods?
    - What is maxSurge, maxUnavailable?

## 🧱 Terraform

- Q23. Have you used Terraform?
  - Follow-ups:
    - Show module structure.
    - Show provider file.
    - How do you manage remote backend?
    - How do you manage state locking?
    - What is a data block?
    - What is a module block?

## ☁️ AWS Hands-On Services (Round 2)

- Q1. Which AWS services do you have the most hands-on experience with?
  - Follow-ups:
    - EC2?
    - IAM?
    - VPC?
    - S3?
    - RDS?
    - CloudWatch?
    - Are you confident in these?
    - Have you worked on cost optimization?

## 🔐 IAM & Policies

- Q2. Create an EC2 IAM role that allows access only to S3 + DynamoDB and denies access to all other services.
  - Follow-ups:
    - What is the logic behind a custom policy?
    - What is "Explicit Deny"?
    - How would you restrict everything except two services?
    - Which policy pattern do you use (Allow + NotAction Deny)?

## 💰 Cost Optimization

- Q3. What exact cost optimization steps have you implemented?
  - Follow-ups:
    - What was the % saving?
    - Have you used Reserved Instances or Savings Plans?
    - Do you know cost of ALB vs private ALB?
    - Which scenario costs more?

## 🔁 ALB Cross-Communication

- Q4. Two apps in same VPC → each behind a public ALB → if App A calls App B, how does traffic flow?
  - Follow-ups:
    - Does it go out to internet?
    - Does it come back through IGW?
    - Which option is costlier, public or private ALB?
    - What stays inside VPC vs what leaves?

## 📈 Auto Scaling — Memory & Disk

- Q5. How do you create auto scaling policies based on memory & disk usage?
  - Follow-ups:
    - Are memory and disk metrics available by default?
    - Why do we need CloudWatch Agent?
    - How do you configure the agent?
    - Where do you create CloudWatch alarms?
    - Do you need to update Launch Template?

## 🪣 S3 — Lifecycle + Versioning

- Q6. In a versioned bucket, how do you delete objects + all older versions after 10 days?
  - Follow-ups:
    - What options appear in lifecycle rules?
    - Do we explicitly delete previous versions?
    - What is the difference between Current vs Previous versions?

## 🧮 RDS Troubleshooting

- Q7. App is slow → you suspect RDS. What do you check?
  - Follow-ups:
    - CPU? Memory? Latency? IOPS? Connections? Disk queue depth?
    - Slow query logs? Error logs? Performance Insights?
- Q8. You found memory pressure on RDS. You cannot resize. What immediate action can you take without downtime?
  - Follow-ups:
    - Can you kill heavy queries?
    - Remove idle connections?
    - Create a read replica?
    - Which action applies instantly?
    - Which action causes 0 downtime?

## 🌐 VPC & Networking

- Q9. Request comes from Internet → enters VPC through IGW → what is the first security layer? NACL or SG?
  - Follow-ups:
    - Why NACL first?
    - Which one is stateless?
    - Which one is stateful?
    - Which takes precedence if conflict?
- Q10. If NACL denies a CIDR, but SG allows same IP, can the IP access LB?
  - Follow-ups:
    - Why not?
    - Which one checks traffic first?
    - How many IPs does /32 allow?
    - Does IP X fall in CIDR Y?
- Q11. Does IP 10.11.7.44 fall under 10.11.0.0/16?
- Q12. Does IP 10.11.44.76 fall under 10.1.0.0/16?
- Q13. What does /32 represent?
  - Follow-ups:
    - How many IPs in /32?
    - Which exact IP?
    - How to calculate whether an IP is inside a CIDR block?

## ⚙️ CI/CD — Branch-Based & Rollback

- Q14. Repo has 3 branches: dev, staging, prod. How do you ensure pushing to staging triggers only staging deployment?
  - Follow-ups:
    - Separate pipelines or single pipeline?
    - Use of branch conditions?
    - Environment variables?
    - Webhooks?
    - Should pipeline constantly “check” repo?
    - What type of Jenkins job is best?
- Q15. Have you ever set up rollback in CI/CD?
  - Follow-ups:
    - How do you implement automatic rollback?
    - What triggers a rollback?
    - Is rollback handled by CI/CD or Kubernetes?
- Q16. Have you integrated SonarQube in your CI/CD pipeline?
  - Follow-ups:
    - How to get Sonar token?
    - Where to store token?
    - How to insert Sonar scanner stage?
    - What is quality gate?
- Q17. If a Jenkins job starts but gets stuck, how do you debug?
  - Follow-ups:
    - Check console logs?
    - Node resources?
    - Agent logs?
    - External API calls?
    - When do you restart agent?

## 🧱 Terraform Advanced

- Q18. Terraform generated RDS password, you didn’t save it. Can you retrieve it?
  - Follow-ups:
    - Where does Terraform store generated values?
    - Local state or remote backend?
    - Why is storing secrets in plaintext dangerous?
- Q19. Do you know what a custom Terraform module is?
- Q20. What does a module contain?
- Q21. What is in main.tf?
  - Follow-ups:
    - variables.tf?
    - outputs.tf?
    - providers.tf?
    - How do you call a module from root module?
