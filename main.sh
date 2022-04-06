docker volume new $1
docker build -t $1 .
docker run $1