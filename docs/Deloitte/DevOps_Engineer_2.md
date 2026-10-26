---
company: "Deloitte"
role: "DevOps Engineer"
interview: 2
experience: "4 years"
tags:
  - interview
  - company/deloitte
  - role/devops-engineer
  - topic/kubernetes
  - topic/docker
  - topic/terraform
  - topic/aws
  - topic/ci-cd
  - topic/jenkins
  - topic/security
---

# Deloitte — DevOps Engineer (Interview 2)

Experience note: Linkedin.

## Round 1: Technical Screening

- Explain the CI/CD workflow you follow and the kind of pipeline you use. How do you define and invoke pipelines in Jenkins?
- What are shared libraries in Jenkins, and how are they written and defined?
- What kind of applications do you deploy using Jenkins pipelines, and what deployment tools do you use?
- If the Jenkins pipeline runs but the build doesn’t happen, what possible issues could be causing it?
- What is the purpose of a webhook, and how is it used in a CI/CD pipeline?
- How do you create and manage Kubernetes clusters (using tools like Terraform), and what are the master and worker nodes?
- What are common Kubernetes errors you’ve faced (like CrashLoopBackOff, ImagePullError), and how did you resolve them?
- What is the command to access a pod and how can you define or create a Kubernetes class or object?
- Explain the folder structure of a basic Helm chart. What commands do you use to deploy with Helm?
- What are the stages in a Docker image build? Why do we use ENTRYPOINT and CMD instructions?
- How do you manage and connect services like DBs, EC2, EKS, or ECS? Include the command to connect to ECS.
- Which container registry do you use for storing Docker images?

## Round 2: In-depth Technical Screening

- What branching strategy do you follow, and how do you handle merges to avoid breaking the release branch? If a bug appears in production, what’s your approach to resolving it?
- Describe your typical deployment flow and CI/CD workflow. What stages do you define in your Jenkins pipeline, and how do you ensure full quality checks during deployment?
- How do you use Jenkins shared libraries? Explain their typical structure and how they are integrated into your Jenkinsfiles.
- Are you aware of security scanning tools? How do you scan Docker images—both during build and at the registry level? Are you using any extensions or tools for image scanning?
- How do you pass environment variables during Docker build commands? What services do you use for storing Docker images?
- How do you establish a connection with databases in your deployments or infrastructure setup?
- How do you handle authentication for EKS clusters and store secrets securely in your environment?
- How do you create AWS Lambda functions and manage the artifacts for deployment? What options do you use to push artifacts to Lambda?
- What is email signing and Helm chart signing? Which tools do you use to sign Helm charts?
