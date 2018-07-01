FROM python:3.6.4

# set working director
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app 

# copy the requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

# Install requirements
RUN pip install -r requirements.txt

# copy application files
COPY . /usr/src/app

# Run the app
CMD ["./entrypoint.sh"]