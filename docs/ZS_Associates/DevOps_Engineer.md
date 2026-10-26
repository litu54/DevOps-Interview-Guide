---
company: "ZS Associates"
role: "DevOps Engineer"
experience: "6 years"
tags:
  - interview
  - company/zs-associates
  - role/devops-engineer
  - topic/kubernetes
  - topic/docker
  - topic/terraform
  - topic/aws
  - topic/ci-cd
  - topic/networking
  - topic/databases
---

# ZS Associates — DevOps Engineer

- Multi stage docker build. In which scenarios it would be useful. Is is suitable for compile based language?
- Layer caching, explain with an example
- Privileged mode in Docker. Explain with an example
- Design an architecture for the scenario: if I type <www.application.com> it should get resolved to the backend service
- Calico and VPC CNI plugin difference. Why one is preferred over other. How would they help in setting up networking for pod.
- How is an ip address allocate to a pod. Does CNI plugin use same CIDR range which is provided by VPC or different?
- Two pods which are part of same replica set are not able to communicate with each other what may be the reason
- How to handle the extra traffic coming onto pods? Which solution you can implement
- After implementing HPA also some pods are in pending state. What maybe the reason
- How would you provision karpenter. What all things are needed in configuration
- Can you deploy mongo db database in EKS cluster. If yes how and what all configuration things you would need to keep in mind
- There are 3 backend pods in 3 different region. If one pod goes down how would the request be managed
- Suppose we configured a load balancer but it’s not accepting HTTPS request what would you do?
- Without installing certificate how would you divert the traffic coming from http to https
- How would karpenter know which node to provision. How would it get to know about resource constraints
- Possible reasons for pod to be stuck in Crashloopbackoff
- A backend pod needs to interact with S3 and lambda. How would you achieve it
- How would the service account know which role to assume. What all things you would need to configure in the service account
- Ingress, Gateway API
- A replica set has 3 pods. One pod is not coming up. What maybe be the reason
- Argo CD. How do you manage CI/CD in your organisation. How many EKS clusters you manage, no of nodes
- How do you implement state locking in terraform
- For each in terraform. Explain with an example
- If you want to deploy EC2 instances in 3 different region what would the terraform code structure look like
- questions on modules
- I have made some changes in the module for one resource, the resource should get updated but it should not get destroyed and recreated again when we do terraform apply. How would you approach
- Want to create a module for EKS cluster. What would be the structure
