---
company: "Amazon"
role: "DevOps Consultant"
interview: 2
experience: "7 years"
tags:
  - interview
  - company/amazon
  - role/devops-consultant
  - topic/kubernetes
  - topic/terraform
  - topic/aws
  - topic/networking
  - topic/security
  - topic/scripting
  - topic/databases
---

# Amazon — DevOps Consultant (Interview 2)

Candidate profile: DevOps Consultant.

- If you’re migrating a monolithic application from on-prem to Cloud and the system has its local file system, which file system you will use in AWS
- How will you store all the configurations related to your monolithic app in Cloud
- What are the observibility needed for app —> Monitoring, Alerting, Logging, Remediation, PD
- If you’re not allowed to install Filebeat in your worker nodes for logging, then what will be possible option
- What are the security protocols will be taken into consideration while designing three tier architecture
- DB migration, how will you sync the data
- If DB POD is down, will it affect the data it gets stored
- How about the sticky session data if POD gets down → Yes the session data will be lost
- What service to use sticky session as an alternative option → redis
- During a sticky session problem what will be the cause for LB
- Do you create clusters in multi regions, is it possible? If yes, then how will you manage them
- Onboarded trading app into AWS, how will you make sure availability, scalability, security
- How will you take a back of your entire cluster regulary ?
- Write a python script to list the EC2 instances running in your cloud which has the tag of PROD
- You have been tasked to create 20 EC2 per account and you been provided with 10 AWS accounts, so totally you need to create 200 EC2 machines, how will connect all these machines. Which service will be used?
- You need to connect your DB running in private subnet, not using NAT gateway or NAT instance or bastion host, what are the other options
- Explain about OSI model
- Diff between directory & mount
- Diff between local and variable in Terraform
- You created couple of resources using Terraform, how will you make sure that resources are not modified through UI, how will you automate this check
