#   _ _ _                                __,                        _ __              _      
#  ( / ) )      /o            o  /  o   (                 o        ( /  )       /)o  //      
#   / / / _  __/,  __,  , , ,,  /< ,     `.  _  _   _  ,_,  _, _    /--'_   __ //,  // _  _  
#  / / (_(/_(_/_(_(_/(_(_(_/_(_/ |_(_  (___)(/_/ (_/ |/  (_(__(/_  /   / (_(_)//_(_(/_(/_/ (_
#                                                                            /)              
#                                                                           (/               

build:
	docker build . -t locust

# Open Locust with your profiler script
#
# Usage: make run \
#			SERVICE_NAME="proton" \
#			SERVICE_PORT="32285" \
#
# export MINIKUBE_HOST := $(shell minikube ip) on linux hosts
export MINIKUBE_HOST := host.docker.internal
run:
	@echo $$MINIKUBE_HOST
	docker run \
	-p "8089:8089" \
	--entrypoint "locust" \
	locust \
	-f services/${SERVICE_NAME}.py --host=http://${MINIKUBE_HOST}:${SERVICE_PORT} \
	>> report-${SERVICE_NAME}.log