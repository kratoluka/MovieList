# Movie List
Backend application in Django to display a list of movies loaded from API.  
Application runs in docker to enable use of crontab for periodic tasks.  
Periodically loads a list of movies from API into sqlite3 database.  
Displays a simple front-end to show the movies from database and their information.  
Allows for sorting a filtering of movies.  
  
Run `docker-compose up` to start the docker.  
  
Crontab job is executed every minute and saves its output to `/cron/django_cron.log` within docker.  
This file can be viewed using `docker exec MovieList cat /cron/django_cron.log` while the docker is running.  
