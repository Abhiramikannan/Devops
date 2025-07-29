Qn.Create a ReplicaSet named dns-rs-cka with 2 replicas in the dns-ns namespace using the image registry.k8s.io/e2e-test-images/jessie-dnsutils:1.3 and set the command to sleep 3600 with the container named dns-container .

Once the pods are up and running, run the nslookup kubernetes.default command from any one of the pod and save the output into a file named dns-output.txt .

Ans:

1. create deployment yaml file
2. edit the deployment file to replicaset
   <img width="860" height="644" alt="image" src="https://github.com/user-attachments/assets/9694a042-3791-400a-b98e-9985b98076a1" />
3. namespace created
<img width="509" height="60" alt="image" src="https://github.com/user-attachments/assets/cc8b58ef-f71b-49ef-8864-937dbf0c9965" />

  <img width="661" height="236" alt="image" src="https://github.com/user-attachments/assets/96fa8a9a-5964-4c92-a0b6-ee2aa2f25a2f" />

