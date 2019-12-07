#!/bin/bash
celery worker -A app.celery --loglevel=INFO &
gunicorn app:app -w 1