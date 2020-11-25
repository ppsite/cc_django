#!/usr/bin/env bash

set -e

function is_django_installed() {
  hash django-admin &>/dev/null
}

function is_uwsgi_installed() {
  hash uwsgi &>/dev/null
}

function should_migrate() {
  is_django_installed && [[ -z "${DISABLE_MIGRATE}" ]]
}

function should_collect_static() {
  is_django_installed && [[ -z "${DISABLE_COLLECT_STATIC}" ]]
}

function exec_uwsgi() {
  # migrate
  if should_migrate; then
    python manage.py migrate
  fi

  # collect static
  if should_collect_static; then
    python manage.py collectstatic --noinput
  fi

  # uwsgi
  if is_uwsgi_installed; then
    uwsgi --ini "${HOME}"/runtime/uwsgi.ini
  else
    echo " [x] no uwsgi installed, run 'pip install uwsgi' to fix"
  fi
}

{%- if cookiecutter.use_celery.lower() == 'y' %}
function is_celery_installed() {
  hash celery &>/dev/null
}

function is_flower_installed() {
  hash flower &>/dev/null
}

function exec_celery_worker() {
  if is_celery_installed; then
    celery -A {{cookiecutter.project_name}} worker -l INFO
  else
    echo " [x] no celery installed, run 'pip install django-celery' to fix"
  fi
}

function exec_celery_beat() {
  if is_celery_installed; then
    celery -A {{cookiecutter.project_name}} beat -l INFO
  else
    echo " [x] no celery beat installed, run 'pip install django-celery-beat' to fix"
  fi
}

function exec_celery_flower() {
  if is_flower_installed; then
    flower -A {{cookiecutter.project_name}}
  fi
}

{%- endif %}


# 根据环境变量运行进程
if [ ! "${EXEC_CMD}" ]; then
  echo "!!! no exec cmd found, use default: nginx + uwsgi"
  exec_uwsgi
else
  echo "!!! exec cmd ${EXEC_CMD} found"
  case ${EXEC_CMD} in
  uwsgi)
    exec_uwsgi
    ;;
{%- if cookiecutter.use_celery.lower() == 'y' %}
  celery)
    exec_celery_worker
    ;;
  beat)
    exec_celery_beat
    ;;
  flower)
    exec_celery_flower
    ;;
{%- endif %}
  *)
    echo "!!! ${EXEC_CMD} not in [uwsgi, celery, beat], use default: nginx + uwsgi"
    exec_uwsgi
    ;;
  esac
fi
