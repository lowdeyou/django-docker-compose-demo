# Django Local Development with Docker Compose Demo
This Django demo project demonstrates the utilization of [Docker Compose](https://docs.docker.com/compose/) and application of some of the [The Twelve-Factor App](https://12factor.net/) methodology to automate and streamline local Django development to achieve the following benefits:
* Have the project along with all the backing services up and running with only a single command
* Auto-reload Django and Celery on code changes
* Developers can use any tools or operating system they are comfortable with, since the project will run in a Linux environment within Docker regardless
* Debugging capabilities in Visual Studio Code
* Development/Production parity: Ensures that the same backing services used in production is also used during development and staging. Also ensures that all developers are using the same backing services during development. This would prevent the issue of "Hey, it works on my machine, but why does it breaks on yours?"

This demo project is largely inspired by [cookiecutter-django](https://github.com/pydanny/cookiecutter-django), and had reused a number of ideas and implementations from that project. This is a very useful tool for creating a Django project, and for most cases I would recommend that you use this tool as opposed to starting a Django application from scratch.

On the other hand, I also found that cookiecutter-django may include a large number of services and dependencies that I may not need. Hence I created this demo project to demonstrate a simpler, leaner and minimized Django setup, with some differences/additions:
* Single ```settings.py``` file across all deploys
* Visual Studio Code debugging capability
* Auto-reload on code changes for Celery workers

## Background


### Setting up Services for Django Local Development Can Be Time-consuming
When it comes to Django projects there tend to be a tedious initial setup for local development, epecially when the development is to be handed over or shared with other developer(s). For example, prior to local development for a typical Django project, an incoming developer would probably have to do the following:
* Install database server (e.g. PostgreSQL)
* Configure database connectivity to allow remote connection
* Create database and database user(s)
* Install message broker service (e.g. RabbitMQ/Redis)
* Create vhost(s) and user(s) on the message broker service
* Install SMTP server
* Configure SMTP server
* Create email account(s)
* Set up Django configuration values in environment variables for use with Django's ```settings.py```
* Install project dependencies using ```pip install -r requirements.txt```
* Run ```python manage.py migrate``` to initialize the database
* Run ```python manage.py runserver``` to start the development server
* Run ```celery -A project.celery_app worker -l INFO``` to start the Celery workers

Sounds pretty tedious and time-consuming isn't it? Certain Django projects require even more services such as Elasticsearch and Apache Kafka, which probably increase the amount of steps needed to be performed. Additionally, more often than not, there's likely to be errors in the manual setup procedures and the developer would have to go through a whole lot of pain trying to troubleshoot the issue. Overall, this translates to a large amount of wasted man-hours.

This demo project, with the utilization of Docker Compose in combination to applications of some of the [The Twelve-Factor App](https://12factor.net/) methodology, will demonstrate how to effectively streamline the entire development process.


### Identified Caveats
* Auto-reload may not work properly for Docker for Windows running under WSL2 backend. To rectify this, configure Docker to switch to using Hyper-V instead of WSL2.


## Running the Project
### Requirements
Ensure you have the following installed:
* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Quickstart
To get this project up and running, simply clone this project and then run the following command in the project's root folder:
```
docker-compose -f dev.yml up
```
That's it!
### Running Commands
The Django application will be running within Docker container, hence to run Django commands, you can do it like so:
```
docker-compose -f dev.yml run --rm django python manage.py migrate
docker-compose -f dev.yml run --rm django python manage.py makemigrations
docker-compose -f dev.yml run --rm django python manage.py createsuperuser
docker-compose -f dev.yml run --rm django python manage.py shell
```


### EXTRA: Quickstart with Visual Studio Code Debugging
Since the application runs in Docker, it may seem we would lose the debugging capability that coding tools offer. Here, the project demonstrates that debugging is still possible, using the Visual Studio Code as example.

Run Docker Compose command as per Quickstart above, but include ```-f dev_vscode_debug.yml```:
```
docker-compose -f dev.yml -f dev_vscode_debug.yml up
```

Once the services are up, in Visual Studio Code (with this project opened), go to Sidebar > Run section. On the top of the panel that appears, choose either ```Django: Remote Attach``` or ```Celery: Remote Attach``` and then click on Start Debugging to begin debugging the application.





