heroku config:set APP_SETTINGS=config.Development
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=uptsurabayaterbaik2020
heroku run sh migrate.sh
heroku run sh migrate.sh