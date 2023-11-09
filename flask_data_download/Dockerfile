FROM mcr.microsoft.com/devcontainers/base:ubuntu AS base

WORKDIR /app

RUN sudo apt-get update
RUN sudo apt-get install python3-pip -y

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]  