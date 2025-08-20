@REM for docker container tests:
docker pull mongo:latest
docker run --name my-mongo -p 27017:27017 -d mongo:latest
