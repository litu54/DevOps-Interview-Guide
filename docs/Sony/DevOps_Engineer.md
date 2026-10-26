---
company: "Sony"
role: "DevOps Engineer"
tags:
  - interview
  - company/sony
  - role/devops-engineer
  - topic/kubernetes
  - topic/terraform
  - topic/aws
  - topic/ci-cd
  - topic/jenkins
  - topic/monitoring
  - topic/sre
---

# Sony — DevOps Engineer

1. How would you respond to a production outage during peak hours?
2. So how do you guarantee zero downtime deployments in Kubernetes.
3. How do you decide to roll back or apply a hot‑fix when a production issue occurs?
4. How would you design a system to survive if one AWS region goes down?
5. How would you investigate a sudden three‑times increase in the AWS bill?
6. How can you shorten a CI/CD pipeline that currently takes 45 minutes?
7. How do you stop broken code from reaching production?
8. How do you start troubleshooting when a Kubernetes cluster feels slow?
9. How do you guarantee zero‑downtime deployments in Kubernetes?
10. What steps do you take when monitoring metrics say the system is healthy but users are still complaining?
11. How do you design alerting so that you avoid noisy or false alerts?
12. How do you design alerting to avoid alert fatigue?

- I want jenkins run pipeline once n number of commits are pushed how will you do that.
- What are the vulnerability reports in your sonarqube.
- If I want to start an ec2 instance once the cpu is utilised 80% what terraform code will you write and it also should copy the image from S3.
- How will you secure your jenkins pipelines.
- How would you design a Kubernetes cluster that must survive a full AZ failure without data loss, while running stateful workloads at scale? (Storage, networking, controllers, quorum, recovery)
- Explain the complete request flow when using Gateway API with multiple GatewayClasses across regions. How do you prevent split-brain routing?
- How do you debug intermittent pod restarts when liveness probes pass, readiness passes, but the pod is still killed by the node?
- What happens internally when etcd latency spikes above 500ms? How does it impact the scheduler, controllers, and API server?
- Design a multi-tenant Kubernetes platform where teams must not affect each other’s resource usage, network traffic, or upgrade cycles.
- How would you implement zero-trust networking inside Kubernetes without using a service mesh?
- Describe a real production incident where a misconfigured HPA caused cascading failure. How would you redesign autoscaling to avoid this?
- How do you safely refactor a Terraform monorepo with hundredsgg of state files into a module-based architecture without downtime?
- Explain how Terraform handles dependency graphs internally. How can circular dependencies still appear in real projects?
- How would you manage Terraform when multiple teams deploy to the same AWS account but must not overwrite each other’s resources?
- Describe a production failure caused by terraform apply. What guardrails would you implement to prevent it permanently?
- Why does a container sometimes exit immediately even though the application works perfectly in local testing? Give 3 real production causes.
- How would you design container images for ultra-fast cold starts in serverless or autoscaled Kubernetes environments?
- How do you design GitOps for 1000+ clusters with environment drift detection, emergency hotfixes, and controlled manual overrides?
