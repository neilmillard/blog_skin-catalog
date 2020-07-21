#!/bin/sh
# . /var/www/webroot/virtenv/bin/activate && \
#    python ../get-poetry.py && \
#    . /var/www/webroot/.poetry/env && \
#    poetry config virtualenvs.create false && \
#    poetry env info && \
#    poetry install
cd sc_blog || exit


# migrate on database
echo "about to run migrate on the database"
python manage.py migrate --noinput

# create default groups with permissions
echo "creating groups and permissions"
python manage.py creategroups

# create django super user with "$DJANGO_SUPERUSER_EMAIL"
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python manage.py createsuperuser --no-input)
fi

if [ -n "$STATIC_ROOT" ] ; then
  # create static files
  echo "create static files into $STATIC_ROOT"
  python manage.py collectstatic --noinput --clear
fi

# .env file write
#echo "writing .env file"
#cat >.env <<EOL
#SECRET_KEY=${SECRET_KEY}
#DATABASE_URL=${DATABASE_URL}
#ALLOWED_HOSTS=${ALLOWED_HOSTS}
#STATIC_ROOT=${STATIC_ROOT}
#EMAIL_HOST_USER=${EMAIL_HOST_USER}
#EMAIL_HOST_PASSWORD=${EMAIL_HOST_PASSWORD}
#RECAPTCHA_SECRET_KEY=${RECAPTCHA_SECRET_KEY}
#EOL

echo "deploy.sh complete"
