# flashcards
Flashcards App that uses docker-compose based development environment.

## Development
The local webapp directory is mounted as a volume within the web container.

Launch the environment
```
docker-compose up -d
```

## Push to heroku

You will need to create a heroku app before being able to push the containers
```
heroku app:create appname-identifier

e.g. heroku app:create flashcards-8980
```

To push the app to production
```
heroku container:push web -a <app name>

e.g. heroku contianer:push web -a flashcards-8980
```