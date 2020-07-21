init:
	pip install poetry
	cd sc_blog && \
		poetry install

dev: init
	cd sc_blog && \
		export SECRET_KEY="some-random-value-420" && \
		export RECAPTCHA_SECRET_KEY="some-random-value-420" && \
		export GOOGLE_ANALYTICS="" && \
		export DATABASE_URL="sqlite:///db.sqlite3" && \
		export ALLOWED_HOSTS="localhost" && \
		export STATIC_ROOT="" && \
		poetry run python manage.py migrate && \
		poetry run python manage.py runserver --settings=sc_blog.settings.development
