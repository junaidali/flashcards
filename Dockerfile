#Grab the latest alpine image
FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

# Install python and pip
ADD ./webapp/requirements.txt /tmp/requirements.txt

# Updated pip
RUN pip3 install --upgrade pip

# Install dependencies
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    && pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp

# Generate static content
RUN python manage.py collectstatic

# Expose is NOT supported by Heroku
# EXPOSE 5000 		

# Run the image as a non-root user
RUN adduser -D myuser
USER myuser

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn --chdir mysite --bind 0.0.0.0:$PORT mysite.wsgi:application

