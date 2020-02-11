.PHONY: serve cover test

serve:
	gunicorn --reload wsgi:app


cover:
	pytest --cov=markdownserver tests


test:
	pytest tests
