# Nyuseu :: News :: 뉴스

News reader in [Python](https://www.python.org) and [Django](https://www.djangoproject.com/)


![Main page](https://github.com/foxmask/nyuseu/blob/master/nyuseu/doc/screenshot.png)

## :package: Installation

### Requirements

* Python > 3.10
* Django < 4

### Installation

pandoc

```bash
sudo apt install pandoc
```

create a virtualenv

```bash
python3 -m venv nyuseu
cd nyuseu
source bin/activate
```

install the project

```bash
pip install nyuseu
```


##  :wrench: Settings

copy the sample config file

```bash
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

```bash
cd nyuseu
python manage.py createsuperuser
python manage.py migrate
```

## :mega: Running the Server
### start the project

```bash
python manage.py runserver localhost:8001
```

then, access the project with your browser http://127.0.0.1:8001/

### Manage your data

go to http://127.0.0.1:8001/admin and enter the login/pass of the created `superuser`

### :eyes: Importing OPML file

enter the following command

```bash
python opml_load.py /path/to/the/file.opml
```

eg

```bash
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

### :eyes: Exporting OPML file

enter the following command

```bash
python opml_dump.py /path/to/the/file.opml
```

eg

```bash
Nyuseu :: 뉴스 :: News - Feeds Exported in file foobar.opml
```

### get the update of your news

in your crontab add this for example

```bash
*/59 * * * * cd ~/Projects/nyuseu/ && . bin/activate && cd nyuseu && ./manage.py nyuseu_update
```

(Image credits to [Emojipedia](https://emojipedia.org/))

## Board creation

![Board creation 1](https://github.com/foxmask/nyuseu/blob/master/nyuseu/doc/create_1.png)

![Board creation 1](https://github.com/foxmask/nyuseu/blob/master/nyuseu/doc/create_2.png)

## accessing to boards

![My boards](https://github.com/foxmask/nyuseu/blob/master/nyuseu/doc/my_boards.png)
