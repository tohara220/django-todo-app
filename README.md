# django-todo-app

Django で構築した TODO アプリ

## 使い方

サーバの起動

```bash
gunicorn --bind 0.0.0.0:8000 --access-logfile - core.wsgi:application
```
