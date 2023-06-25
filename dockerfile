FROM nvidia/cuda:11.4.0-base-ubuntu20.04

ARG http_tmp
ARG https_tmp
ENV http_proxy=$http_tmp
ENV https_proxy=$https_tmp

RUN apt-get update --fix-missing && apt-get install -y python3 python3-pip git screen tmux

COPY ET-BERT/requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt