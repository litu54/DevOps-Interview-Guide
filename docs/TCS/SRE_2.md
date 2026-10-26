---
company: "TCS"
role: "SRE"
interview: 2
tags:
  - interview
  - company/tcs
  - role/sre
  - topic/kubernetes
  - topic/docker
  - topic/terraform
  - topic/databases
---

# TCS — SRE (Interview 2)

Gemini company interview questions

- What is Terraform drift?
- Difference between COPY and ADD commands in a Dockerfile.
- If a Docker image becomes very large with many layers, what steps would you take to reduce its size?
- If you have 10 layers in a Dockerfile and layer 6 fails, after fixing it, where will the rebuild start from and why?
- Difference between bind mounts and volumes in Docker.
- Why do we need a StatefulSet when we can attach a PVC to a Deployment and make it stateful?
- If a pod is created with a Deployment and another with a StatefulSet, will the StatefulSet pod always remain on the same node?
- If we can run MySQL with a Deployment and PVC, why do we need a StatefulSet?
- What happens if we scale a Deployment with one PVC from 1 to 3 replicas?
- What types of services exist in Kubernetes, apart from ClusterIP, NodePort, and LoadBalancer?
- Why does a pod created from a Deployment have two sets of random characters in its name?
