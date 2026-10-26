---
company: "JPMorgan"
role: "DevOps SRE"
experience: "5 years"
tags:
  - interview
  - company/jpmorgan
  - role/devops-sre
  - topic/kubernetes
  - topic/terraform
  - topic/aws
  - topic/azure
  - topic/ci-cd
  - topic/monitoring
  - topic/sre
  - topic/networking
  - topic/security
---

# JPMorgan — DevOps SRE

Candidate profile: Devops/SRE.

1) What would you say is your strongest skillset area in DevOps/SRE and which technologies do you want to focus on going forward?
2) Your application is currently running on EC2 instances in a public subnet. How would you migrate it to a private subnet without any downtime? Explain the complete approach. if it doent work how would u rollback?
3) You have two running pods in a Kubernetes cluster, but they are unable to communicate with each other. There are no errors in the logs or events, and both pods appear healthy. How would you troubleshoot and restore communication between them?
4) If a pod’s liveness or readiness probe is failing, how would you troubleshoot the issue?
5)  Apart from  actuator health-check endpoints, what other checks can you perform using Kubernetes probes?
6) If an application has only one replica and you perform a rolling restart, will there be downtime? Also what events occur during the pod restart can you explain the sequence step by step?
7) You have an application with 2 replicas. During a rollout, the first pod is successfully replaced, but when the second pod is being replaced it enters a CrashLoopBackOff state. At that moment, which pod will the load balancer route traffic to the new pod, the old pod, or both? explain
8) Just like we use code-quality and security checks (quality gates, OWASP) before building an image, how can we prevent insecure infrastructure changes from being pushed using terraform?

    - For example, if someone modifies a security group in Terraform and opens it to 0.0.0.0/0, what mechanisms can we use in Terraform to stop such changes from being applied?

9) How would you handle Terraform state management for a team? Specifically, how would you store the tfstate file securely, make sure only one person can modify it at a time, and ensure the state is not tampered with? give me answers for all 3 qns
10) You’ve joined a company where a large production infrastructure was built manually and the previous engineers have left. How would you bring that existing infrastructure under Terraform management? Walk me through your plan
11) Are you aware of the recent AWS and Azure outages? What were your key takeaways from those incidents?
12) If an entire region goes down and even a multi-cloud setup (like AWS + Azure) experiences outages how would you ensure that your data is still safe and not lost? What strategies would you use to guarantee reliable backups and recovery?
13) What components or agents are typically installed along with Prometheus, and what does each of them do?
14) In an EFK/ELK stack, what does each component do and how does the overall pipeline work? Additionally, how do filtering and indexing work inside Elasticsearch?
15) Do you have any questions you would like to ask me?
