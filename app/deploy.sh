#!/bin/bash
imageName = $1
if docker ps -a --format "{{.Names}}" | grep -q "counter-service"; then
  echo "Container 'counter-service' found."
  docker stop counter-service || echo "Error stopping container 'counter-service'."
  docker rm counter-service || echo "Error removing container 'counter-service'."
else
  echo "Container 'counter-service' not found."
fi

docker pull $imageName || echo "Error pulling image $imageName."
docker run -d -p 80:80 --name counter-service $imageName || echo "Error starting container 'counter-service'."

