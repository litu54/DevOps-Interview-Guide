---
company: "Sigmoid"
role: "DevOps Engineer"
interview: 2
experience: "7 years"
tags:
  - interview
  - company/sigmoid
  - role/devops-engineer
  - topic/kubernetes
  - topic/terraform
  - topic/monitoring
  - topic/networking
  - topic/security
  - topic/databases
---

# Sigmoid — DevOps Engineer (Interview 2)

Candidate profile: DevOps Engineer.

- Terraform taint
- How to limit the resource usage in K8s
- asked me to write request and limit usage YAML file
- Write a deployment file for the below requirement
  - Create a Deployment named 'space-alien-welcome-message-generator' of image 'httpd:alpine' with one replica.
  - It should've a ReadinessProbe which executes the command 'stat /tmp/ready' . This means once the file exists the Pod should be ready.
  - The initialDelaySeconds should be 10 and periodSeconds should be 5

- If Liveness probe is healthy and readiness probe is failing, what will happen
- How will you find out the data loss while switching back to DBs
- Have you integrated Global LB with K8s cluster
- How to enable RBAC to Service accounts
- You created a resource through Terraform but it failed during provision, what will happen
- Purpose of using "null resource" in Terraform
- If some developer hardcoded password mistakenly in source code and pushed to repo, how to fix it in CI process
- If terraform deployment got failed, what will be the approach
- Write a script to capture the failures

  Input :

  ```text
  2025-05-23 10:00:01 ERROR: Connection failed to database
  2025-05-23 10:01:02 INFO: Retrying connection
  2025-05-23 10:01:30 ERROR: Connection failed to database
  2025-05-23 10:02:10 ERROR: Connection failed to database
  2025-05-23 10:03:55 ERROR: Connection failed to database
  2025-05-23 10:06:00 INFO: Recovery attempt successful
  2025-05-23 10:07:20 ERROR: Timeout while reading from API
  2025-05-23 10:08:15 ERROR: Timeout while reading from API
  2025-05-23 10:09:10 ERROR: Timeout while reading
  ```

  output :

  ```text
  [ALERT] 'Connection failed to database' occurred more than 3 times
  [ALERT] 'Timeout while reading from API' occurred more than 3
  ```

- DNS Custom resolver
- Metrics used for monitoring
