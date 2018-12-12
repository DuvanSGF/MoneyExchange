# Introduction
----
ChangeHouse was developed by Duvan Mejia, with the documentation available on docs.djangoproject.com.
---

[![Build Status](https://travis-ci.org/FineUploader/fine-uploader.svg?branch=master)](https://github.com/DuvanSGF/changehouse)
[![npm](https://img.shields.io/npm/v/fine-uploader.svg)](https://docs.npmjs.com/getting-started/what-is-npm)
[![CDNJS](https://img.shields.io/cdnjs/v/file-uploader.svg)](https://cdnjs.com/libraries/file-uploader)
[![license](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/DuvanSGF/changehouse/blob/master/LICENSE.TXT)
[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/Duvancortes_mc.svg?style=social&label=Follow%20%40Duvancortes_mc)](https://twitter.com/Duvancortes_mc)

[**Documentation**](#documentation) |
[**Examples**](#running-tests) |
[**Support**](../../issues) |
[**Changelog**](../../releases)

---

This package officially supports all currently supported versions of Python/Django:

|      Python   | 2.7 | 3.3 | 3.4 | 3.5 | 3.6 |
| :------------ | --- | --- | --- | --- | --- |
| Django 1.10   |  :white_check_mark:  | :x: |  :white_check_mark:  |  :white_check_mark:  | :large_blue_circle: |
| Django 1.11   |  :white_check_mark:  | :x: | :white_check_mark:   | :white_check_mark:   | :x:                 |
| Django 2.0    |  :large_blue_circle:                 | :white_check_mark: | :white_check_mark:   | :white_check_mark:   | :white_check_mark:                 |
| Django [master](https://github.com/django/django/archive/master.tar.gz) | :x: | :x: | :x: | :x: | :x: |

| Key |                                                                     |
| :-: | :------------------------------------------------------------------ |
| :white_check_mark: | Officially supported, tested, and passing                           |
| :large_blue_circle: | Tested and passing, but not officially supported                    |
| :white_square_button: | Not officially supported, may break at any time, most tests passing |
| :x: | Known incompatibilities                                             |

Authored by [Duvan Mejia](https://stackoverflow.com/users/9872532/duvan-sgf?tab=profile).

----
## Documentation

* [Requirements](#requirements)
* [Installation](#installation)
* [Configuration](#configuration)
  * [Migration Configuration](#migrations-configuration)
  * [Run Migrations](#run-migrations)
* [Notes](#notes)
* [Future](#future)
* [Running Tests](#running-tests)
* [License](#license)

----

## Requirements
* Python 3.6.6
* Django 2.0



## Installation

Clone this repository into your project:

```bash
git clone https://github.com/DuvanSGF/changehouse.git
```

Download the zip file and unpack it:

```bash
wget https://github.com/DuvanSGF/changehouse/master.zip
unzip master.zip
```

pip install -r requirements.txt
./manage.py migrate
./manage.py runserver



## Configuration

You'll need to see the documentation If you not understand something. See that [documentation](https://docs.djangoproject.com/en/2.0/) for guidance.

You'll need to add `estudiantes` to `INSTALLED_APPS` in your projects `settings.py` file:

```python
INSTALLED_APPS = (
    # ...
    'changehouse',
    # ...
)
```

### Migration Configuration

These settings should be reviewed and set or modified BEFORE any migrations have been run.


### Run Migrations

After you have configured all migration settings, run

```bash
python manage.py migrate changehouse
```
then

```bash
python manage.py makemigrations changehouse
```



### Import Configuration

These settings should also be reviewed and set or modified before importing any data.



## Notes

If you is here! Congrats only two steps more and it's ready!

I'm finding some bugs and I will fix.



## Future 

* I'm working about that! 



## Running Tests

1. Install postgres, MySQL (In my case I have installed XAMPP).
2. Create `changehouse` database.
3. Run the following command :

        $ python manage.py createsuperuser
        Username: admin

        You will then be prompted for your desired email address:
        Email address: admin@example.com

4. Run tests:

        $ python manage.py runserver

        Now, open a Web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/site/. You should see the admin’s login screen:

 <img src="https://raw.githubusercontent.com/RamEduard/admin-lte-express/master/public/readme/login.png" width="300">


## license

MIT, as the original project. See LICENSE.txt.
