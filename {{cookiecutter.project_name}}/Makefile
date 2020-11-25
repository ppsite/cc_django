clean:
	rm -rf db.sqlite3
	{%- if cookiecutter.use_account.lower() == 'y' %}
	rm -rf account/migrations
	{%- endif %}
	{%- if cookiecutter.use_demo.lower() == 'y' %}
	rm -rf project/migrations
	{%- endif %}
