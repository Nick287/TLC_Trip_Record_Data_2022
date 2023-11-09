FROM mcr.microsoft.com/devcontainers/base:ubuntu AS base

RUN sudo apt-get update
RUN sudo apt-get install python3-pip -y

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt
