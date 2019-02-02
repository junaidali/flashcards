[Build Status]([![Build Status](https://travis-ci.org/junaidali/flashcards.svg?branch=master)](https://travis-ci.org/junaidali/flashcards))


# flashcards
Flashcards App that uses docker-compose based development environment.
The project includes a Makefile to help with common administration tasks.

## Setup Heroku Platform
Install the Heroku CLI using instructions available on [Heroku Documentation](https://devcenter.heroku.com/categories/command-line)

### Login to Heroku
You will need to login to heroku to use the CLI
```
heroku login -i
```

### Login to Heroku Container Platform
You will need to login to heroku container registry to push and release images
```
heroku container:login
```

### Create a new application with postgres support
You will need to create a new app on heroku
```
heroku create
```
This will generate an MYAPPNAME for your application. You will need to pass this to the heroku push stage.

Add postgres support
```
heroku addons:create heroku-postgresql:hobby-dev -a MYAPPNAME --wait
```

Verify the postgres database
```
heroku pg:info -a MYAPPNAME
```

## Development
The local webapp directory is mounted as a volume within the web container.

Launch the environment
```
make run
```

## Push to heroku
You will need to create a heroku app before being able to push the containers
```
make publish APPNAME=MYAPPNAME
```

To push the app to production
```
make release APPNAME=MYAPPNAME
```