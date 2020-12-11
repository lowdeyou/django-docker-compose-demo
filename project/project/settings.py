import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

# If you want to use .env file instead of environment variables for the rest
# of your config, set this environment variable to 'true'
READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    environ.Env.read_env()

SECRET_KEY = env('DJANGO_SECRET_KEY')

DEBUG = env.bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[
                         "localhost", "127.0.0.1"])

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = ['crispy_forms']

LOCAL_APPS = ['invitation.apps.InvitationConfig']

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    'default': env.db()
}

EMAIL_CONFIG = env.email_url('DJANGO_EMAIL_URL')
vars().update(EMAIL_CONFIG)

# Email address to be displayed as sender in sent emails
DEFAULT_FROM_EMAIL = env.str("DJANGO_DEFAULT_FROM_EMAIL")

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": ("django.contrib.auth.password_validation."
                 "UserAttributeSimilarityValidator"),
    },
    {
        "NAME": ("django.contrib.auth.password_validation."
                 "MinimumLengthValidator"),
    },
    {
        "NAME": ("django.contrib.auth.password_validation."
                 "CommonPasswordValidator"),
    },
    {
        "NAME": ("django.contrib.auth.password_validation."
                 "NumericPasswordValidator"),
    },
]

CELERY_BROKER_URL = env.str("DJANGO_CELERY_BROKER_URL")

TIME_ZONE = env.str("DJANGO_TIME_ZONE", default="UTC")

LANGUAGE_CODE = "en-us"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

CRISPY_TEMPLATE_PACK = "bootstrap4"
