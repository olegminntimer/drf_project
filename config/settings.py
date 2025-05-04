import os
import sys
import certifi
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

os.environ["SSL_CERT_FILE"] = certifi.where()

SERVER_TYPE = os.environ.get("SERVER_TYPE", "")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG", "False") == "True"

# if not SECRET_KEY and not DEBUG:
#     raise ValueError("SECRET_KEY must be set in production")

# ALLOWED_HOSTS = ["*"]
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",") if os.getenv("ALLOWED_HOSTS") else []
if DEBUG:
    ALLOWED_HOSTS.extend(["localhost", "127.0.0.1", "0.0.0.0"])

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_yasg",
    "users",
    "lms",
    "django_filters",
    "django_celery_beat",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

if 'test' in sys.argv or os.getenv('GITHUB_ACTIONS') == 'true':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'test_db.sqlite3',
        }
    }
else:
    # if SERVER_TYPE == "local":
    #     host_db = "127.0.0.1"
    # else:
    #     host_db = "db"

    # Установлены fallback-значения для переменных окружения, чтобы не вызвать ошибки, если они не заданы.
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DB", "postgres"),
            "USER": os.getenv("POSTGRES_USER", "postgres"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD", "postgres"),
            "HOST": os.getenv("POSTGRES_HOST", "localhost"),
            "PORT": os.getenv("POSTGRES_PORT", "5432"),
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=20),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")


REDIS_HOST = "redis" if os.getenv("DOCKER_ENV") == "true" else "127.0.0.1"
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:6379/1",
    }
}

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:6379/0"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:6379/0"

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": "redis://redis:6379/1",
#     }
# }
#
# # Настройки для Celery
#
# # URL-адрес брокера сообщений
# CELERY_BROKER_URL = "redis://redis:6379/0"  # Например, Redis, который по умолчанию работает на порту 6379
#
# # URL-адрес брокера результатов, также Redis
# CELERY_RESULT_BACKEND = "redis://redis:6379/0"

# Часовой пояс для работы Celery
CELERY_TIMEZONE = TIME_ZONE

# Флаг отслеживания выполнения задач
CELERY_TASK_TRACK_STARTED = True

# Максимальное время на выполнение задачи
CELERY_TASK_TIME_LIMIT = 30 * 60

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
# Настройки для Celery
CELERY_BEAT_SCHEDULE = {
    "task-check_last_login": {
        "task": "lms.tasks.check_last_login",  # Путь к задаче
        "schedule": timedelta(
            hours=1
        ),  # Расписание выполнения задачи (например, каждые 10 минут)
    },
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "False") == "True"
EMAIL_USE_SSL = not EMAIL_USE_TLS and (os.getenv("EMAIL_USE_SSL", "False") == "True")
if EMAIL_USE_TLS and EMAIL_USE_SSL:
    raise ValueError("EMAIL_USE_TLS and EMAIL_USE_SSL cannot be both True")

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Настройки для production
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    SESSION_COOKIE_HTTPONLY = True
