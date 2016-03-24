# build a new container image
docker build -t flask-sample-one:latest .  

#run the container on port 80
docker run -d -p 80:80 flask-sample-one
