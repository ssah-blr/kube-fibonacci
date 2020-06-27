# Kube-Fibonacci 
Simple Fibonacci Application written in Python, meant for Kubernetes Cluster, with instruction to create Docker Image files.

![Alt text](kubefibonacci.jpg?raw=true "Kube Fibonacci")

Prerequisites -

	1. DockerHub Account with repository named fibo (e.g. <DockerhubAccount>/fibo). Login to hub.docker.com -
           docker login -u <DockerhubAccount>
	2. Kubernetes Cluster with DNS sollution like CoreDNS

Step 1. Build Docker Images -

Docker image for HTML web app (Flask based python Application) - 

	cd Dockerfiles/v6web/
	sudo docker build -t v6web .
        #Make note of ImageID from above docker build command, and use in next command
	sudo docker tag <ContainerImageID> <DockerhubAccount>/fibo:v6web
	sudo docker push <DockerhubAccount>/fibo:v6web

Docker image for Main app. Python API, accepts GET request and responds in json format.

	cd Dockerfiles/v6app/
	sudo docker build -t v6app .
        #Make note of ImageID from above docker build command, and use in next command
	sudo docker tag <ContainerImageID> <DockerhubAccount>/fibo:v6app
	sudo docker push <DockerhubAccount>/fibo:v6app

Step 2. Create Kubernetes objects. The web application reaches main app by resolving DNS entry of ClusterIP service. Check script 'Dockerfiles/v6web/fibonacci.py'.
Note: Update your Docker Account name <DockerhubAccount> in declaration file KubeDeployments/fibonacci/fibonacci.yaml (at 2 places).

	cd KubeDeployments/fibonacci
	kubectl create -f fibonacci.yaml

Step 3. Access application, by accessing woker node Ip -

        Nodeport=$(kubectl get svc -l app=fiboweb -o jsonpath="{.items[0].spec.ports[0].nodePort}")
        Browse -> http://<workernode-IP>:$Nodeport

Screenshot of applicaiton on browser -
![Alt text](Screenshot.jpg?raw=true "Kube Fibonacci")

Thanks
Sanjay
