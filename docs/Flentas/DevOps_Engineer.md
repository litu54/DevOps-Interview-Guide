---
company: "Flentas"
role: "DevOps Engineer"
experience: "3.5 years"
tags:
  - interview
  - company/flentas
  - role/devops-engineer
  - topic/kubernetes
  - topic/docker
  - topic/terraform
  - topic/aws
  - topic/ci-cd
  - topic/jenkins
  - topic/git
  - topic/networking
  - topic/databases
---

# Flentas — DevOps Engineer

Interview Questions for Flentas (3.5 Years Experience)

1. What is your architecture in your current project?
2. What applications are deployed in the frontend and backend?
3. Why did you not deploy the frontend on S3 and CloudFront, and instead deployed it on EKS?
4. What is a namespace in EKS?
5. How many namespaces do you currently have?
6. What is a node group?
7. How do you perform cost optimization on ECS, RDS, and ElastiCache?
8. Why have you used RDS Proxy?
9. The client application did not have connection pooling — how did you handle it?
10. A node is unable to join the cluster. What could be the reason?
11. What is the difference between the control plane and the data plane?
12. What is the difference between a Pod and a Container?
13. What are requests and limits in Kubernetes?
14. One node has 8 vCPU and 32 GB RAM. With pod autoscaling up to 4 replicas, each pod having limits of 4 vCPU / 16 GB and requests of 2 vCPU / 10 GB RAM, how many instances of the pod will run?
15. What did you implement in Lambda and API Gateway?
16. What is the difference between Redis and Memcached?
17. Explain the Terraform folder structure.
18. What is the difference between Terraform and Terragrunt?
19. What is the state file in Terraform?
20. How do you handle resource dependencies in Terraform?
21. When you ran terraform apply, did you encounter any unexpected changes?
22. If there is a problem in Terraform, how will you roll back the changes?
23. I have created an LB using Terraform, and some updates happened on it. Now I want to delete the LB only — how will you do it?
24. How do you handle secrets in Terraform?
25. How will you pass secrets from AWS Secrets Manager to the pipeline?
26. Do you commit the tfvars file to Git? While running the pipeline, these parameters need to be filled — how do you manage this in Jenkins?
27. What is Docker?
28. What is the difference between an image and a container?
29. What is a Helm chart?
30. I want to enable autoscaling in Kubernetes during high traffic. How will you scale both cluster nodes and pods?
31. Can we use Cluster Autoscaler?
32. How do you scale EC2 instances?
33. When do we use VPA (Vertical Pod Autoscaler)?
34. Have you upgraded the EKS cluster?
