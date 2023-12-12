# # set base image (host OS)
# FROM python

# # Author
# LABEL author="Sandro Sanchez"

# # set the working directory in the container
# WORKDIR /code

# # copy the dependencies file to the working directory
# COPY requirements.txt .

# # install dependencies
# RUN pip3 install -r requirements.txt

# # copy the content of the local src directory to the working directory
# COPY src/ .

# command to run on container start
# CMD [ "python", "/app.py" ]

#Use the latest ubuntu image
FROM ubuntu:latest

# Author
LABEL author="Sandro Sanchez"

# Run a system update and install python
RUN apt-get update && apt-get install -y python3 \
    python3-pip

# Create a new system user
RUN useradd -ms /bin/bash smss6

# Change to this new user
USER smss6

# Set the container working directory to the user home folder
WORKDIR /home/smss6/code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy the content of the local src directory to the working directory
#COPY src/ .


