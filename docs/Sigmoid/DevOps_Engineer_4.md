---
company: "Sigmoid"
role: "DevOps Engineer"
interview: 4
experience: "4–7 years"
tags:
  - interview
  - company/sigmoid
  - role/devops-engineer
  - topic/kubernetes
  - topic/docker
  - topic/terraform
  - topic/aws
  - topic/ci-cd
  - topic/jenkins
  - topic/ansible
  - topic/linux
  - topic/monitoring
  - topic/sre
  - topic/networking
  - topic/security
  - topic/scripting
  - topic/databases
---

# Sigmoid — DevOps Engineer (Interview 4)

## Round 1 (F2F technical - whiteboard round)

1. Give introduction
2. The flow from dev to prod. What are the security checks that you follow within CI pipeline of your current project.
3. What is the branching strategy that you follow in your org. Why did you follow this approach over other strategies.

4. There is a new requirement from platform team to design a 3 tier architecture, with frontend , backend and database with all the security best practices , high availability , low latency. (AWS) As a Devops engineer , you have to make a decision according to best and optimized solution for each component that you decide, like - should the db be run as statefullset or RDS/any cloud db managed solution is better, how do we deploy frontend-whether as pod or S3+cloudfront etc.

5. During the explanation of architecture there were many counter and followup questions -
    1. How can you tell a subnet is pubic or private, what things needs to be in place.
    2. How is an end user able to access the app which is running inside pods of private subnet nodes.
    3. What is route53, how does the traffic actually flow in order, if a user requests or submits or posts anything from the UI.
    4. Explain each component in your architecture which is involved from a user requesting from the UI to the request reaching the backend pod, and how they are connecting with each other to ensure inbound and outbound flow(including the firewall, NACl, security groups, route tables etc).
    5. If you used a service with type: LoadBalancer and as you told its in private subnet , then how its able to launch a loadbalancer in public subnet, how its getting access to do it from within    private subnet. Which component of the control plane takes care of it.
    6. Why did you choose eks cluster over ecs.
    7. How are you managing the cluster nodes.
    8. For your specific architecture setup, how many ip addressess for all the components do you think will be sufficient enough from all the available IP's of both subnets within your VPC.
    9. Tell me how you handle the situation, if there is a DDoS attack in your cluster nodes or the cluster services, which is consuming all resources at 100% . What steps do you take in order to regain the condition back and what steps do you take to prevent this in future.
    10. How are you handling HA in your cluster , explain the reason why you use a specific feature over the other similar functionalities.
    11. What is the requirement of NAT gateway in your cluster, where should it placed to make it work as intended.

6. Write a script to find a particular name in a file and replace it with another word.(can use bash or python) - they asked to execute as well
7. Write a script to just find the first occurance of a pattern in the given file , and then extract the full line of the found pattern.(can use bash or python) - they asked to execute as well
8. Write a script to find all the files in current directory and all subdirs,which are modified more than 5 hours ago, but not beyond today.

## Round 2(F2F technical round with cloud devops architect)

1. Write python script to reverse string without using loop , without slicing shortcut, without in-built functions/libraries.
2. Write a python script to take an integer input(input should handle only for atleast 2 digits), check divisibility by only 3 or by only 5 or by both 5 and 3 with proper handling, like if its divisible by both then it should not return the single divisibility, it should only return divisibility by both. If divisible by none of 3 or 5, check if its a prime number, if not a prime as well, then find all the numbers by which its divisible excluding itself and 1 and return the list of them.

3. Explain and draw the architecture diagram of your current project flow end to end, while also explaining the measures you have taken for ensuring the security and best practicies to comply with SLA.
4. In your current project , how are you handling the CI integration for multiple environments like dev/test/qa/staing/prod.
5. Which branching strategy are you following and how did you apply this strategy to integrate within your CI pipeline to deploy the pushed code to the right env cluster. Where exactly in your CI code you handled deploying to dev , and to QA and so on till its ready for production. How did you handled the PR checks and approvals in your CI pipeline.
6. What are the activities that happen after deploying to each env of CI pipeline and before its ready for next environment.
7. Did you use AWS accounts? How did you handle the segregation of various environments within AWS.
8. How is data block different from resource block in terraform. Explain a scenario in which both of them are used in conjunction.
9. There is a requirement as part of some new integration in terraform managed resources, where couple of resources needs to be completely out of terraform lifecycle and they completely need to be handled manually. Come up with a solution to approach this without causing disruption to those resources, so that they are untouched and are not destroyed while also making it independant resource.
10. What is taint in terraform, give a scenario where you need to use taint , explain how it works.
11. Explain what are terraform workspaces, what is the main requirement to use them.
11. There was an issue last time with some config changes in TF resource which had lead to slight downtime of the AWS resource during apply. What might have caused this downtime, how do you handle this in terraform for futurue config changes, for ensuring least possible downtime and maximum possible availability. Write a terraform code to handle this situation.
12. Explain the S3 lifecycle. What are classess in S3.
13. Did you work on cloudfront. How did you leveraged this for exposing frontend static code to serve the UI of the app.
14. What is k8s API. Can you connect to a k8s API using REST api calls directly from any external app, like how kubectl connects to the API endpoints exposed on the kube API server?
15. If there was an issue introduced in recent deployment , then how do we rollback the deployment , is it just the kubectl rollout undo command , how does it know which image it should revert to,does it take from the image repo or somewhere else?

## Round 3 (F2F managerial + technical round)

1. Explain the use of below linux commands:

   finger,comm, netstat, jq, yq, at, atq, shuf, lsblk, less, last, nc, mtr, iftop, lsof, blkid, mkfs, nice

2. Write a python script which takes a user input with any alphabet in capital (the user inp should be strictly alphabet and shouldn't be small letters).Then, from a given file, find min, max, sum from the corresponding numbers of the input alphabet. After printing the above details, delete all those matched lines from the file.

   eg:

   ```text
   file.txt
   C,23
   A,41
   A,67
   Q,44
   C,29
   B,88
   A,12

   If input=A, then min = 12, max = 67 , sum = 120
   If input=B, then min = 88, max = 88 , sum = 88
   ```

3. We have an app log updating in realtime, which contains multiple IP addresses who attempted connecting to it. Can you write a python script to return all the unique IP addresses from the log along with total count of unique ip addresses?

   eg:

   ```text
   app.log
   Connection established from : 145.11.21.78
   Connection established from : 189.22.99.19
   Connection established from : 145.11.21.78

   output should be: 145.11.21.78 , 189.22.99.19 , count=2
   ```

4. Write a 3 stage Dockerfile with below scenario using pre-built images that they provided for each stage
   1. Set and copy the env config files , env variables , bash profiles like .bashrc , .bashprofile etc which already comes with image, to the 2nd stage
   2. Use the files from previous stage and perform some prerequisite tasks and build the code from the current directory
   3. Use the output from the previous stage and build image

5. Explain how is the image creation happening ,what are layers, how are layers forming, what details will we have in the image which is created from the final stage.
6. What steps/commands in the Dockerfile is creating intermediate images. Once the final image is created , are these intermediate images still being utilized ?

7. What is the difference between CMD and ENTRYPOINT. Explain with a scenario, how and why we use both of them in conjunction.
8. What if we have multiple CMD's and ENTRYPOINT's in a single Dockerfile, would we get issues/errors during the docker build? If there is no issue in build , then how does docker takes care of these multiple CMD and ENTRYPOINT lines in Dockerfile while building it.

9. What is publisher in Jenkins.
10. What are executors in jenkins. Explain how they are working under the hood.
11. Please explain how did you setup sonarqube in your CI jenkins pipeline, what are the quality gates and how did you set the threshold checks for code coverage leveraging the test reports created by developer.

12. In Ansible playbook, how do you pass the output of one task to the next, especially when you're working with different blocks or stages in a playbook? For example, if you have multiple blocks, each with its own output, how can you transfer the results from one block to another—like from the first block to the second, or even from the 4th block to the tasks that come after?

13. Why do we need extra load balancing capabilities like host based, path based routing etc to our pods, if services are anyways handling the traffic to route to right pod, what actuslly is the issue where just tradional standalone service cannot handle it. For example, if an end user is traversing accross various product details , how is frontend able to fetch details from the right pod (backend which in turn gets the actual product data from db), explain how the api calls to backend and to db is handled.

14. If there is a real time application like a multiplayer game, or streaming app, how does it handle heavy concurrent user sessions at the same time without any latency and without too much delay.

15. Consider a live production app which you are managing, and suddenly it started having latency issuues on the customer side where they are seeing slownes on each request to get processed and see the updates/response on UI back with lot of lag (lets say from 5 ms normal latency to suddenly ~5 mins). How would you go ahead with your troubleshooting, do a deep RCA to find out the exact source of issue, and you are given the task to resolve it in very short time as this is very critical app.

16. Write a PromQL expression to alert if CPU usage is above 80% on any node.
17. How will you alert if CPU usage stays above 90% for 5 minutes, but only if the number of running pods is below 5?

18. Custom resource vs custom resource definitions

19. Explain the end to end setup of ELK stack in the cluster that you are working on, in your current ongoing project.
20. How is kibana connecting to Elasticsearch, write a yaml snippet  where this connectivity is handled.
21. What are operators in kubernetes. How is the Elasticsearch working , is there some Elastic operator involved?

22. Consider there is a MySQl operator running in one of your pod in one of your node of a k8s cluster. How the Mysql database managed by this is different from the normal pod that is started with a mysql image from deployment/pod template? Apart from just handling the updates, version changes, lifecycle, vulnerabilitites , security issues, it provides lot more advantages, please explain the use cases by giving some scenarios.

23. If there is a requirement to run fixed 1 Mysql database accross each one of the nodes, how can you set this up in your cluster, with the help of custom operators.
