#!/bin/bash

NAME="mysite"                                   # Name of the application
DJANGODIR=/home/shahbazz/app/react-django/backend               # Django project directory
SOCKFILE=/home/shahbazz/app/react-django/backend/run/gunicorn.sock  # we will communicte using this unix socket
USER=shahbazz                                         # the user to run as
GROUP=shahbazz                                        # the group to run as
NUM_WORKERS=3                                       # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=mysite.settings      # which settings file should Django use
DJANGO_WSGI_MODULE=mysite.wsgi              # WSGI module name
echo "Starting $NAME as `whoami`"

# Activate the virtual environment

cd $DJANGODIR
source env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
