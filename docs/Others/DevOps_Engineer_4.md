---
company: "Unknown"
role: "DevOps Engineer"
interview: 4
tags:
  - interview
  - role/devops-engineer
  - topic/kubernetes
  - topic/terraform
  - topic/aws
  - topic/git
  - topic/security
---

# Undisclosed company — DevOps Engineer (Interview 4)

- how you ensure the best possible security for high availability architectures for 3 tier applications.
- Diff b/w SGs and NACLs.
- what is VPC peering.
- How do you scan the vulnerabilities specially for AWS instances.
- diff between IAM Users and Roles
- Can you avoid the specific port traffic using SGs?
- How you connect to private instances when the SSH connection is not working?
- where do you use firewalls, SGs and NACLs
- What are the best password security practices used by your organisation?

- What are the security parameters we must consider while we are creating an EC2 instance for production?
- How can you protect the data in an AWS instance?
- How can you connect from AWS to on-prem servers?
- Explain about the transit gateway and why do we use this?
- What are the provisioners available in Terraform and can you explain the use cases?
- I have created an EC2 instance named A, and I want to create another instance B. It should create an instance without deleting instance A. What can I do during this?
- I have created an EC2 instance through Terraform. I don't have a backup of the Terraform state file, it is not in the remote state and locally not available. Now when I do apply, what can I do?
- Suppose I have given one command in null resource, it should run every time. What is the behavior?
- What is the difference between a map of objects in Terraform and how can you write an example?
- Suppose in your DevOps team, new team members are added to your team. How can you provide AWS access to your new users, what is the behavior of login to the console?
- What is the difference between an EBS-backed instance and a non-EBS-backed instance?
- I have 3 nodes (small, medium, and large), and I want only data load to go to the large node. How can I do that?
- When I deploy the pods, it should be deployed on large and medium. Nodes, except small. How can I configure that?
- I am getting the following error, how can I debug that and what does the error mean?

  ```text
  Pods fail to schedule
  0/5 nodes are available: insufficient memory.
  ```

- What is the difference between scaling and autoscaling in Kubernetes?
- If I don't specify TargetPort in the service object, what is it going to do?
- What are the different types of secrets in Kubernetes?
- I have an Ingress object that is not routing the traffic to the Kubernetes cluster. What are the reasons and how do you troubleshoot that?
- I have created a service object that is not mapped to a deployment. What could be the reason and how do you debug it?
- What are the different ways to specify the probes in Kubernetes?
- What is the difference between git push --force-with-lease vs --force?
- If I select the restart policy as Never, what is it going to do?
- What is an init container and why do we need to use it?
- What is the difference between EKS vs ECS vs Fargate?
- How can you delete the last 2 git commits?
