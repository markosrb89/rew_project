FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /rew_project
WORKDIR /rew_project
ADD requirements.txt /rew_project/
RUN pip install -r requirements.txt
ADD . /rew_project/