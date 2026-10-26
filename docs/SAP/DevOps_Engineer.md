---
company: "SAP"
role: "DevOps Engineer"
experience: "8 years"
tags:
  - interview
  - company/sap
  - role/devops-engineer
  - topic/kubernetes
  - topic/ci-cd
  - topic/jenkins
  - topic/git
---

# SAP — DevOps Engineer

Candidate profile: Devops.

- Suppose a new deployment was implemented, suddenly all the PODs (new and old ones) crashed, what's the reason for this ? → New deployment exhausted the resource limit, so we need to use "limit" in our deployment.yaml file
- Which deployment is better cost wise.
- I want my deployment to be implemented to specific workloads or regions, that update shouldn't go to other parts. There is an option in argo CD
- How the auto scaling works, how things work in the back-end, from worker nodes to master nodes. Communication track behind that.
- Can we perform Blue Green deployment under the same namespace? If yes, how will you manage them?
- You did a deployment with Canary, when you will delete the old pods, what are the KPIs to cross check before deleting them.
- Once the blue green deployment is completed, how to check if the deployment is successful.
- You’re trying to schedule a new POD but the new PODs are not deploying properly, what checks will be done.
- Why do you want to use Argo CD over Jenkins?
- How will you maintain your base image, vulnerability free?
- How will you perform the patches regularly
- Git submodules, what is their purpose
