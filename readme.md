# Syarat.ID Source Code

Syarat.ID is a content aggregator website that gathering all informations with the specific keyword: "syarat" from the internet.

SEO and Performance

![Syarat Measure](/static/syarat-measure.png)

![Syarat Pingdom](/static/syarat-pingdom.png)


This repository contains source code from the [syarat.id](https://www.syarat.id) site.

To run this project on your own local machine, please follow the installation steps below:

```bash
# clone to your local machine 
$ git clone git@github.com:syarat/syarat.git
$ cd syarat

# create your own virtual environment
$ python -m venv env

# install the project dependencies
$ pip install -r requirements.txt

# run makemigrations and migrate 
$ ./manage.py makemigrations
$ ./manage.py migrate

# create a superuser
$ ./manage.py createsuperuser

# load the dummy data
$ ./manage.py loaddata fixtures/db.json

# run the server
$ ./manage.py runserver

# DONE
```

Fixing error that comes from `django-compressor`
```bash
$ pip install rjsmin --install-option="--without-c-extensions"

$ pip install rcssmin --install-option="--without-c-extensions"
```


For contributing, please open an issue or make your own change and create a PR.

