# A myweb Flet app

An example of a minimal Flet app.

To run the app:

# Running the app locally
flet run --web --port 8000 main.py

# Running the app in production

## Build the Docker image
$ docker build -t my-python-app .

## Run the Docker container
$ docker run -d -p 8189:8000 --restart=always --name web --hostname web my-python-app

$ docker run -d -p 8189:8000 --restart=always --USER_LOGIN=admin --PASSWORD_LOGIN=123 --name web --hostname web my-python-app

$ docker run -it --rm --name my-running-app my-python-app


# docker build -t my-python-app .

# docker run my-python-app