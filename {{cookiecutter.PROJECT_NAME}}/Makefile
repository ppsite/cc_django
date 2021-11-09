env="dev"

make:
	python manage.py makemigrations account
	python manage.py migrate
use:
	python utils/env.py use --params $(env)
clean:
	rm -rf db.sqlite3
	rm -rf account/migrations

