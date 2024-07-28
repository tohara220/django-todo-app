import os

SECRET_KEY = ""

DEBUG = False

ALLOWED_HOSTS = ["your-production-domain.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "django_todo_app"),  # データベース名
        "USER": os.environ.get("DB_USER", "uninsho"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "pninsho"),
        "HOST": os.environ.get("DB_HOST", "db"),  # dbはdocker-composeのサービス名
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
