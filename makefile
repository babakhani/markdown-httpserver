.PHONY: serve cover test

serve:
	gunicorn -t999999 --reload --reload-extra-file markdownserver/master.mako wsgi:app


cover:
	pytest --cov=markdownserver tests


test:
	pytest tests
