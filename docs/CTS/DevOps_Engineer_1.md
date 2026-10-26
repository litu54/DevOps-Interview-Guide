---
company: "CTS"
role: "DevOps Engineer"
interview: 1
tags:
  - interview
  - company/cts
  - role/devops-engineer
  - topic/terraform
  - topic/networking
  - topic/security
---

# CTS — DevOps Engineer (Interview 1)

- What is connection drain
- Backend.tf file is showing in repo but it is not showing in storage account, what may be the issue
- How to login VM if VM has private IP
- You have deployed a web app and it was working fine but application went down, and all networking are fine and related ports are open, how to troubleshoot
- Types of load balancers
- What is Az App Gateway and how it encrypt http/https traffic
- App is down and throwing 503 err code, what steps should be taken

- Also for question 4 is the answer the below?
- Check the status of nginx/apache service that was used to host the web app
- Check if any firewall/security group rules are blocking the flow of traffic
- Ping/telnet won't make sense since networking side is fine
- Clearing cache/cookies from browser for stale enteries
- Do nslookup for dns resolution if that works fine
- Check SSL certificate if it has gone corrupt and is working fine
- Lack of memory on the web app server due to which it is failing to load the resources for the app
