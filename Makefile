.PHONY: build run stop clean publish release

define DJANGO_SETTINGS_HEROKU_CONFIG

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
endef
export DJANGO_SETTINGS_HEROKU_CONFIG

build:
	@echo "Building Containers"
	@docker-compose build

run:
	@echo "Running Containers"
	@docker-compose up -d

stop:
	@echo "Stopping Containers"
	@docker-compose stop

clean:
	@echo "Removing Containers"
	@docker-compose rm -f

publish:
	@echo "Publishing Containers to Heroku"
	@echo "Backup current settings.py"
	@cp webapp/mysite/settings.py webapp/mysite/settings.py.bak
	@echo "Adding Heroku config"	
	@echo -e "$$DJANGO_SETTINGS_HEROKU_CONFIG" >> webapp/mysite/settings.py
	@heroku container:push web -a flashcards-123
	@echo "Revert settings.py"
	@mv webapp/mysite/settings.py.bak webapp/mysite/settings.py

release:
	@echo "Releasing Containers to Heroku"
	@heroku container:release web -a flashcards-123