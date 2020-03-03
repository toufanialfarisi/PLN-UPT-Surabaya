rm -r migrations
rm db.sqlite
export FLASK_APP=run.py
export APP_SETTINGS='config.Development'
flask db init
flask db migrate
flask db 
python lab.py
