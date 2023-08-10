#!/bin/bash
if docker ps -a --format "{{.Names}}" | grep -q "counter-service"; then
  echo "Container 'counter-service' found."
  docker stop counter-service || echo "Error stopping container 'counter-service'."
  docker rm counter-service || echo "Error removing container 'counter-service'."
else
  echo "Container 'counter-service' not found."
fi

docker pull $1 || echo "Error pulling image $1."
docker run -d -p 80:80 --name counter-service $1 || echo "Error starting container 'counter-service'."

