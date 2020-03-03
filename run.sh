. envi/bin/activate
echo "environment was activated"
export APP_SETTINGS='config.Development'
echo "APP_SETTINGS variable was exported"
gunicorn run:app -b 0.0.0.0:5001 --reload --workers 2 --log-level=debug