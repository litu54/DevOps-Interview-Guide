---
company: "HCL"
role: "DevOps Engineer"
interview: 3
experience: "5 years"
tags:
  - interview
  - company/hcl
  - role/devops-engineer
  - topic/kubernetes
  - topic/terraform
  - topic/aws
  - topic/ci-cd
  - topic/networking
---

# HCL — DevOps Engineer (Interview 3)

- Landing zone, guard trail, scp, control tar. —— interviewer ask for this vocabulary ❌ (general)
- Account 1 to Account 2 – send AMI but its KMS encrypted, help me do that ❌ (aws)
- EC2 has IAM roles, what all things can we explore from it ✅ (aws)
- I have EC2 and S3 in same subnet, region how to access that bucket from instance ✅ (aws)
- I have EC2 instance, internet connectivity not there, how to tackle this ❌ (aws)
- Two instances are there what is the best way to communicate with them, create new NIC or attach ❌ (aws)
- I have multiple IAM user which is best approach: 1. attach policy individual to user OR 2. add that user to group and attach policy ✅ (iam)
- Inline policy or attaching policy which is right approach ❌ (iam)
- Have you used permission boundaries ❌ (-)
- S3 lifecycle rules – what is the advantage of using them ✅ (s3)
- Have you worked on transit gateway ❌ (-)
- ALB and NLB have you used it ✅ (aws)
- Public and private subnet is there, NAT gateway is attached to private subnet what is use of that (masking of private ip) ✅ (vpc)
- How does NAT gateway protect my private subnet, what concept does it use to secure the resource (same masking) = masking is protecting the private subnet ✅ (vpc)
- KMS, Secrets Manager have you worked on it ❌ (aws)
- Manually EC2 updated from t3.medium to t3.large manually and updated the code and committed but pipeline not ran. If you run pipeline then what will happen? (nothing will happen – code is in local machine of devops) ✅ (aws)
- Can you use same build spec used in AWS CodeBuild ✅ (terraform)
- Wat is DaemonSet in Kubernetes and what default daemons comes up with Kubernetes ✅ (kubernetes)
- An init container comes up with the Kubernetes cluster ✅ (kubernetes)
- Taint and toleration in Kubernetes what it is ❌ (kubernetes)
- Compute reservation in manifest files ❌ (kubernetes)
