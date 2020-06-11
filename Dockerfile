FROM python:3.6 

RUN apt-get update && apt-get install build-essential -y 

RUN pip install locust

WORKDIR "/srv/profile"

COPY --chown=65533:65533 [".", "."]

ENTRYPOINT ["locust", "-f", "profile.py", "--host=http://192.168.99.102:31994"]