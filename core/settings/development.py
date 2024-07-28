import os

from .base import BASE_DIR

DEBUG = True

ALLOWED_HOSTS = []

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
#     # "default": {
#     #     "ENGINE": "django.db.backends.postgresql",  # PostgreSQLを使用
#     #     "NAME": os.environ.get("DB_NAME", "django_todo_app"),  # デフォルト値を指定
#     #     "USER": os.environ.get("DB_USER", "tohara"),  # デフォルト値を指定
#     #     "PASSWORD": os.environ.get("DB_PASSWORD", "tohara"),  # デフォルト値を指定
#     #     "HOST": os.environ.get("DB_HOST", "db"),  # デフォルト値を指定
#     #     "PORT": os.environ.get("DB_PORT", "5432"),  # デフォルト値を指定
#     # }
# }
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
