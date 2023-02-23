# LAB - Class 31

## Project: Docker Pet Project

###  Author: Natalija Germek Clarke

###  Version:

*Version 1.0* Initial creation of pet project after docker reinstall, README updated, models created, superuser created,
settings updated, admin updated, url file created, initial migrations ran, application created and registered. -
19 January 2023

*Version 1.2* Added url paths in project and app, added views. 

*Version 1.3* Refactoring - 20 February 2023

*Version 1.4* Refactoring complete, updated README.md, docker working with .env and .requirements.txt working. - 22 February 2023

## Links and Resources

[Link to Database](http://0.0.0.0:8000/api/v1/pets/)
[Admin Login Page](http://0.0.0.0:8000/admin/)

## Setup

.venv for virtual environment
.env requirements

PORT - - "8000:8000"
DATABASE_URL - http://0.0.0.0:8000/api/v1/pets/

- How to initialize/run your application 

- > docker-compose up
- > docker-compose down
- > python manage.py runserver
  
Tests
How do you run tests?

python manage.py test 

Link and reminder that admin page is available for those with credentials. You are, however, doing a great job at using your Readme to keep track of your versioning progress.