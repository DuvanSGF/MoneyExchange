# Introduction
----
MoneyExchange was developed by Duvan Mejia, with the documentation available on docs.djangoproject.com.
---
[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.0-brightgreen.svg)](https://djangoproject.com)
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

|      Python   | 2.7 | 3.6 |
| :------------ | --- | --- |
| Django 2.0    |  :large_blue_circle:| :white_check_mark: |
| Django [master](https://github.com/django/django/archive/master.tar.gz) | :x: | :x: | :x: | :x: | :x: |

| Key |                                                                     |
| :-: | :------------------------------------------------------------------ |
| :white_check_mark: | Officially supported, tested, and passing                           |
| :large_blue_circle: | Tested and passing, but not officially supported                    |
| :white_square_button: | Not officially supported, may break at any time, most tests passing |
| :x: | Known incompatibilities                                             |

Authored by [Duvan Mejia](https://stackoverflow.com/users/9872532/duvan-sgf?tab=profile).
![Django Boards Screenshot](https://pbs.twimg.com/media/DuqxoENWkAAj_G8.jpg:large)
----
## Documentation

* [Requirements](#requirements)
* [Installation](#installation)
* [Configuration](#configuration)
  * [Migration Configuration](#migrations-configuration)
  * [Run Migrations](#run-migrations)
* [Notes](#notes)
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
widget https://github.com/DuvanSGF/changehouse/master.zip
```
unzip master.zip


## Configuration

Installing Virtualenv

For the next step, we are going to use pip, a tool to manage and install Python packages, to install virtualenv.

Create the folder: In the Command Prompt, execute the command :
```bash
mkdir changehouse
```

and then :
```bash
cd changehouse
```
and finally in the Command Prompt, execute the command below:

```bash
virtualenv .
```
or
```bash
pip install virtualenv
```

Our virtual environment is installed. Now before we start using it, we need to activate:
```bash
.\Scripts\activate
```

It’s very straightforward. Now that we have the venv activated, run the following command to install requirements:

```bash
pip install -r requirements.txt
```
You'll need to see the documentation If you not understand something. See that [documentation](https://docs.djangoproject.com/en/2.0/) for guidance.


### Migration Configuration

1. Install postgres, MySQL (In my case I have installed XAMPP).
2. Create `changehouse` database.

These settings should be reviewed and set or modified BEFORE any migrations have been run.

### Run Migrations

After you have configured all migration settings, run

```bash
python manage.py migrate
```
then

```bash
python manage.py makemigrations
```



### Import Configuration

These settings should also be reviewed and set or modified before importing any data.



## Notes

If you is here! Congrats only two steps more and it's ready!

I'm finding some bugs and I will fix.


## Running Tests

Run the following command :

```bash
  $ python manage.py createsuperuser
```
Username: Your name

Email address: admin@example.com

Finally, run the development server:

```bash
  $ python manage.py runserver
```

Now, open a Web browser and go to “/site/” on your local domain – e.g., **127.0.0.1:8000** You should see the admin’s login screen:

 <img src="https://raw.githubusercontent.com/RamEduard/admin-lte-express/master/public/readme/login.png" width="300">


## license

MIT, as the original project. See [MIT License](https://github.com/DuvanSGF/changehouse/blob/master/LICENSE.TXT).

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)
