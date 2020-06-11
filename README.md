# Profiling a service

Take alook at https://wikitech.wikimedia.org/wiki/User:Alexandros_Kosiaris/Benchmarking_kubernetes_apps

- Draft a new deployment-charts from service's template
    ```
    ./create_new_service.sh
    ```
- Get latest service's image
- Write locust.io scripts to test endpoints
- Collect data and tweak memory and CPU

```
minikube start
helm repo update
helm init
helm install service-name
```
## Get the service URL  
`minikube service --url <name-of-the-service-pod>`

## Adding secrets to your service
Inspired by https://cloud.google.com/kubernetes-engine/docs/tutorials/authenticating-to-cloud-platform


kubectl create secret generic fcm-key --from-file=key.json=/home/mateus/workspace/wikimedia/infrastructure/fir-test-c2760-firebase-adminsdk-jachy-2cb00aa806.json


## When the pod fail with errors

The following error indicates that the VM is not proper allocating resources, and the only solution I have so far is recreating the environment: `0/1 nodes are available: 1 Insufficient cpu, 1 Insufficient memory.`

Solution:
```
minikube stop && minikube delete && minikube start && helm init
```