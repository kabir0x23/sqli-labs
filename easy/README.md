
```bash
sudo apt install sqlite3

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

sqlite3 sql_injection_easy.db < sql_injection_easy.sql

gunicorn -c gunicorn_config.py app:app
```

