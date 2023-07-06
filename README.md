# Liverpool FC Docker web project - README
## lfc-docker
Liverpool FC Docker web project produced as part of University of Edinburgh/ 
HyperionDev Software Engineering Bootcamp. The website contains two standalone 
pages ('Home' and 'Honours'), a members' area which makes use of a custom
Django user/ authentication solution and a competition area which allows an
admin use to load competition 'posts' and makes use of Django authentication
routines.

DISCLAIMER: this is a personal project and is in no way affiliated with Liverpool
Football Club.  The development of this project is for personal use only, and
any demonstrations of features (e.g. competitions) are exemplars only.

## Table of contents
1. Installation
2. Usage
3. Credits
4. URL

## 1. Installation
* Clone the GitHub repo locally in a folder called 'LiverpoolFC'.
* Ensure you have python3 installed on your machine (details can be found
  [here](https://www.python.org)).
* Set up a virtual environment for the project by running the following commands:
  * python -m pip install pip
  * pip install virtualenv
  * pip install virtualenvwrapper
* For MacOS users, place the following code in your ~/.zshrc file:

```bash
# Setting PATH for Python 3 installed by brew if it is not present
export PATH=/usr/local/share/python:$PATH
# Configuration for virtualenv
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3 export 
VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv source
/usr/local/bin/virtualenvwrapper.sh
```

* Open a command line window and type the following to set up your virtual
  environment and install Django:

```
mkvirtualenv my_django
workon my_django
pip install django
```

## 2. Usage
The website can be accessed by entering the following in the command line:

* Launch the virtual environment using ```workon my_django```
* 

The website can be accessed at ```http://127.0.0.1:8000/```.
&nbsp;

<img width="1400" alt="Liverpool FC Django project home page" src="https://github.com/andrewjbaker/liverpool-fc-web-project/assets/111700184/c894810a-4939-4cf8-ab34-e148546d0dd0">
&nbsp;
 
From the home page you are able to use the navigation bar at the top to 
register as a member and login using your email address and password (see
below), which will enable you to access member area content such as the
live competitions.
&nbsp;

<img width="1400" alt="Django project registration page example" src="https://github.com/andrewjbaker/liverpool-fc-web-project/assets/111700184/9661d1c7-7604-462f-b678-342943a1e6d3">
&nbsp;

<img width="1400" alt="Django project member login information page" src="https://github.com/andrewjbaker/liverpool-fc-web-project/assets/111700184/1980afff-4edc-4824-885c-75f1df12a11e">
&nbsp;
 
### 2.1. Admin functionality
To access the admin functionality, you need to create a superuser account by
entering ```python manage.py createsuperuser``` at the command line.  The 
admin access is available at ```http://127.0.0.1:8000/admin```.
&nbsp;

<img width="1436" alt="Django admin view" src="https://github.com/andrewjbaker/liverpool-fc-web-project/assets/111700184/f253c748-f481-4431-a696-5c61fd105f33">
&nbsp;


## 3. Credits
Developed by Andrew Baker (GitHub: andrewjbaker) as part of the University of 
Edinburgh and HyperionDev Software Engineering Online Bootcamp (2023).

## 4. URL
You can access the repository for this project 
[here](https://github.com/andrewjbaker/liverpool-fc-web-project).
