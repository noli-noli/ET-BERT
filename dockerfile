FROM nvidia/cuda:11.4.0-base-ubuntu20.04

RUN apt-get update --fix-missing && apt-get install -y python3 python3-pip git 