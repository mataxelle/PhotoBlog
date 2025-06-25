# Django WebyApp PhotoBlog

## Table of contents

*  [General info](#general-info)
*  [Development environment](#development-environment)
*  [Install on local](#install-on-local)
*  [Start the environment](#start-the-environment)

## General info

Blog for photographers who want to share their photos. There are two types of users: creators and followers. Only creators should be able to create content. This content should then be shared in a social feed, and followers should be able to choose which creators they want to follow.

## Development environment

- Python 3.10+ recommended
- `pip`

## Install on local

1. Clone the repo on your local webserver : [Repository](https://github.com/mataxelle/PhotoBlog.git).

2. Create a virtual environment (optional but recommended)
```
python -m venv env
env\Scripts\activate (activate the environment)
deactivate (deactivate the environment)
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Apply migrations
```
python manage.py migrate
```

5. Create a superuser
```
python manage.py createsuperuser
```

## Start the environment

```
python manage.py runserver
```
