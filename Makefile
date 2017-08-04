run:
	python manage.py runserver

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

collect:
	python manage.py collectstatic

user:
	python manage.py createsuperuser

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
