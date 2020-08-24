[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ricardorams/event-task-management-app)


**event-task-management-app**

Project: EVENT TASK APP

This project is of the Full Stack Development course that I am taking, provided by Code Institute.
This specific one, is the milestone project of the Full Stack Development Chapter.
The objective of this project is to test and put in practice the techologies and langueges I have learned during the chapter, which are: Python, Django, SQL, Bootstrap, Javascript, HTML, CSS, etc.

The website itself it is a online shop where users can buy tickets for events.

UX:

The user is supposed to find an easy and intuitive interface.

As a User I want to be able to:
Register
Login
Logout
Save pernoanl info
Edit personal info
View events
View venues
View staff
Pay for tickets
View past orders

As an Admin I want to be able to do everything a regular user does plus:]
Add edit and delete, users venues staff and events

FEATURES:

All the previous features mentioned in the UX part, are fully implemented and fully functional. ( chech the techologies part to see how they were implemented )

TECHNOLOGIES USED:

HTML and CSS
Used to display the front-end;

Javascript
Used to implement collapsable menus and form submitions;

Bootstrap
Front end framework. Most of the styling is based on bootstrap;

Python
Used to manipulate back end and front end. This is the "central point" of the project;

Django
Python framework used to implement python and manipulate the project and interactions between components. This is the framework the allows connections between front end files using python;

SQL
Allows for database functionalities;

DJ Database Url:
Allows to parse databse connections;

Flake8:
Helps correcting errors and implementing best practices;

Django Allauth:
Autentication System;

Django Crispy Forms:
Forms;

Stripe:
Payments;

TESTING:
Front-End: I have tested the website using multiple browsers, in this case Chrome, Opera and Safari. I have also tested it in mobile devices of multible size, using Chrome develpor options. (Iphone, Ipad, Samsung Galaxy, etc)
Back-End: I have tested all the links and buttons present in the website, as well as all the input fields. After finishing all this tests I can guarantee that all the CRUD operations are available to the users, without broken links or options.
Flake8: I used Flake8 to test and implement good coding practices and coding standards.
The html css and js code was running through validators with major errors preventing its functioning.
All the input fields were manually tested. 
The website flow (from landing page and login, to the payment), were testing from multiple prespectives and multiple screens.

The main problem that I found during the testing was:
Because of the side of the project, it was possible to test almost everything manually.
With a project possible growing, this would not be possible anymore and a more viable approach would be needed, with more automation.

This project was deployed to Heroku to the following url: https://event-task-app.herokuapp.com/

In order to implement this project in a safe and correct way, some environment variables were needed:

AWS_ACCESS_KEY_ID used to store media and static files
AWS_SECRET_ACCESS_KEY used to store media and static files
DATABASE_URL used for connection to the database
EMAIL_HOST_PASS used for sending emails
EMAIL_HOST_USER used for sending emails
SECRET_KEY used for running django
STRIPE_PUBLIC_KEY used for stripe payments
STRIPE_SECRET_KEY used for stripe payments
STRIPE_WH_SECRET used for stripe payments
USE_AWS used to store media and static files
DEVELOPMENT used to set debug mode

All the variables mentioned above are used in the code but no defined. They are defined in heroku as "Config Vars".
To run the code locally, you should run the "manage.py" file. In order for it to run successful, you will need to define all the variables above. All of them should be defined in the "settings.py" file.

On the Heroku side, I used the Github/Heroku option available on Heroku's website to do the deployment, by doing this I assure that everytime I commit to github, heroku is updated. 
This allows me to have always the most up to date version deployed and available to the user.

To the development itself, I used Gitpod, which allowed me to work with all the technologies mentioned above, without major bugs.

CREDITS

Code Institute: I gained inspiration to this project in the tutorials made available to its students by Code Institute, which are great and with high level of detail. Following this tutorials provides a great level of understanding about the project as well as getting to a nice final results.
Bootstrap: Used to style the project.
Youtube: Used for learning how to implement a count up Javascript timer.
Pexels: Used for gathering free images.
Flake8: Used for best practices.
Stripe: Used for payments.

Ricardo Santos, 2020