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
minikube addons enable metrics-server
```
## Helm package
```
cd /path/to/charts/folder
helm package geoshapes
helm install geoshapes ./geoshapes-0.0.1.tgz
```
### Uninstall package
During development you don't need to keep track of deployments, you just need to uninstall de package and reinstall:
```
helm uninstall geoshapes && helm package geoshapes && helm install geoshapes geoshapes-0.0.1.tgz
```
## Expose the service ports to the local environment
```
kubectl get pods
kubectl port-forward <pod-name> 6534:6534
```
## Open k8s dashboard
```
 minikube dashboard
```
## Create Docker image
`make build`

## Run Profiler
`make run SERVICE_NAME=<service name> SERVICE_PORT=<service port>`
* note: service name must match service names in service directory
* another note: service port comes from the service URL

## Adding secrets to your service
Inspired by https://cloud.google.com/kubernetes-engine/docs/tutorials/authenticating-to-cloud-platform


kubectl create secret generic fcm-key --from-file=key.json=/home/mateus/workspace/wikimedia/infrastructure/fir-test-c2760-firebase-adminsdk-jachy-2cb00aa806.json


## When the pod fail with errors

The following error indicates that the VM is not proper allocating resources, and the only solution I have so far is recreating the environment: `0/1 nodes are available: 1 Insufficient cpu, 1 Insufficient memory.`

Solution:
```
minikube stop && minikube delete && minikube start && helm init
```

### Debug helm templates 
Take a look at this stackoverflow question: https://stackoverflow.com/questions/59564379/how-to-debug-helm-chart-errors-like-error-converting-yaml-to-json-yaml-mappin