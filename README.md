# flask-start
flask-start is a ready-to-use scalable flask architecture for projects of any size. 
It offers a lighter and more flexible alternative to Django.

![](flask-start.gif)


flask-start comes with the following configurations:

- Blueprints (main & errors)
- ORM (SQL-Alchemy + PostgreSQL support)
- Database migration (Flask-Migrate)
- Login (Flask-Login)
- Web Forms (Flask-WTF)
- Mail (Flask-Mail)
- Date & Time rendering (Moment.js & Flask-Moment)
- I18n and L10n (Flask-Babel & Simplified CLI commands)
- Task Queues (Redis & RQ)

flask-start also comes with a simple boostrap sidebar template and custom 404 and 500 error pages.

## Installation

Clone repository
```
git clone https://github.com/alexandre-pecorilla/flask-start
cd flask-start
```

Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```

Set environment variables
```
# add a value for each variable
vim .env.template
# rename file
mv .env.template .env
```

Set flask variables
```
# rename file
mv .flaskenv.template .flaskenv
```

Restart terminal then launch application
```
cd flask-start
source venv/bin/activate
flask run
```
And go to http://127.0.0.1:5000/

For background jobs, also run the following commands in 2 separate terminals
```
redis-server
rq worker main-queue
```

## Dependencies

Python dependencies
```
alembic==1.4.3
Babel==2.9.0
blinker==1.4
certifi==2020.12.5
chardet==4.0.0
click==7.1.2
dnspython==2.0.0
email-validator==1.1.2
Flask==1.1.2
Flask-Babel==2.0.0
Flask-Login==0.5.0
Flask-Mail==0.9.1
Flask-Migrate==2.5.3
Flask-Moment==0.11.0
Flask-SQLAlchemy==2.4.4
Flask-WTF==0.14.3
gunicorn==20.0.4
idna==2.10
itsdangerous==1.1.0
Jinja2==2.11.2
Mako==1.1.3
MarkupSafe==1.1.1
psycopg2==2.8.6
pyenchant==3.2.0
PyJWT==2.0.0
python-dateutil==2.8.1
python-dotenv==0.15.0
python-editor==1.0.4
pytz==2020.5
redis==3.5.3
requests==2.25.1
rq==1.7.0
six==1.15.0
SQLAlchemy==1.3.22
urllib3==1.26.2
Werkzeug==1.0.1
WTForms==2.3.3
```

Optional dependencies
```
# MacOS
brew install redis
# Ubuntu
sudo apt install redis-server
```
For Windows, check the [MicrosoftArchive Redis releases](https://github.com/MicrosoftArchive/redis/releases).

# Credits
Thanks to @miguelgrinberg and his [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
