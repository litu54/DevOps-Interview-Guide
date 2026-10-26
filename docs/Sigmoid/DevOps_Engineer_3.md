---
company: "Sigmoid"
role: "DevOps Engineer"
interview: 3
experience: "7 years"
tags:
  - interview
  - company/sigmoid
  - role/devops-engineer
  - topic/kubernetes
  - topic/docker
  - topic/terraform
  - topic/aws
  - topic/linux
  - topic/scripting
---

# Sigmoid — DevOps Engineer (Interview 3)

- If LB is created in us-south and that region is down what will happen ?
- If RDS is hosted in us-west region and has read replicas spread across other region, due to some issue us-west region is down, how will you redirect your traffic. But having one more DB is expensive to the client
- Which deployment strategy is best, assuming that you have only one POD is running
- If you're going with Blue Green deployment, how will you change your configuration to reroute the traffic between blue and green, exactly which configuration needs to changed?
- New web deployment was done today, how will you make sure that particular application is behaving and we need to find out the issues before user's figures out
- Practical difficulties in having the infra in two different regions
- Write a shell script to delete the log files which is older than 30 days
- Failover mechanism in LB
- Is it possible to have ASG and LB in different regions ?
- How to create sub user while writing Docker file
- Creating custom images
- How to enable Debug logs in Terraform
- Create system design for three tier architecture with secuirty and avalability in place.
- Create a python script for this requirement

  ```text
  #Given a string s, find the length of the longest substring without duplicate characters.

  #Example 1:
  #Input: s = "abcabcbb"
  #Output: 3
  #Explanation: The answer is "abc", with the length of 3.

  #Example 2:
  #Input: s = "bbbbb"
  #Output: 1
  #Explanation: The answer is "b", with the length of 1.

  #Example 3:
  #Input: s = "pwwkew"
  #Output: 3
  #Explanation: The answer is "wke", with the length of 3.
  #Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
  ```
