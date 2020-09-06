# 뉴스 - Nyuseu - News

[![GitHub Action](https://github.com/foxmask/nyuseu/workflows/Python%20package/badge.svg)](https://github.com/foxmask/nyuseu/actions?query=workflow%3A%22Python+package%22) 
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/foxmask/nyuseu/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/foxmask/nyuseu/?branch=master)

News reader in `python 3.8` and `django 3.x`

![Main page](https://github.com/foxmask/nyuseu/raw/master/nyuseu/doc/screenshot.png)

## Prerequistes 

* Python 3.7+
* Django 3+

## Installation
create a virtualenv
```
python3 -m venv nyuseu
cd nyuseu
source bin/activate
```
install the project
```
pip install nyuseu
```
##  :wrench: Settings
copy the sample config file 
```
cp env.sample .env
```
and set the following values
```ini
DEBUG=True   # or False
DB_ENGINE='django.db.backends.sqlite3'
DB_NAME='nyuseu.sqlite3'
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''

TIME_ZONE='Europe/Paris'
LANGUAGE_CODE='en-en'
USE_I18N=True
USE_L10N=True
USE_TZ=True

SECRET_KEY=TOBEDEFINED!

BYPASS_BOZO=True
```

## :dvd: Database
setup the database
```
cd nyuseu
python manage.py createsuperuser
python manage.py migrate
```

## :mega: Running the Server
### start the project
```
python manage.py runserver localhost:8001
```
then, access the project with your browser http://127.0.0.1:8001/

### Manage your data 

go to http://127.0.0.1:8001/admin and enter the login/pass of the created `superuser`

### :eyes: Importing OPML file
enter the following command
```commandline
python opml_load.py /path/to/the/file.opml
```
eg
```commandline
python manage.py opml_load ~/Download/feedly-e2343e92-9e71-4345-b045-cef7e1736cd2-2020-05-14.opml 
Nyuseu Server - 뉴스 - Feeds Reader Server - Starlette powered
Humor Le blog d'un odieux connard
Dev Vue.js News
Dev Real Python
Dev PyCharm Blog
Dev Python Insider
Dev The Django weblog
Dev Ned Batchelder's blog
Dev Pythonic News: Latest
Dev Caktus Blog
Dev The Official Vue News
Android Les Numériques
Android Frandroid
Dys Fédération Française des DYS
Gaming NoFrag
Gaming Gameblog
Gaming Gamekult - Jeux vidéo PC et consoles: tout l'univers des joueurs
Gaming PlayStation.Blog
Gaming jeuxvideo.com - PlayStation 4
Nyuseu Server - 뉴스 - Feeds Loaded
```
