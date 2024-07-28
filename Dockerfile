# ベースイメージ
FROM python:3.11

# DBサービスの起動を待たせるスクリプト
COPY wait-for-it.sh /wait-for-it.sh

# 作業ディレクトリを設定
WORKDIR /app

# Poetryのインストール
RUN pip install poetry

# Poetryの設定：仮想環境を作成しない
RUN poetry config virtualenvs.create false

# 依存関係ファイルをコピー
COPY pyproject.toml poetry.lock* /app/

# 依存関係をインストール
RUN poetry install --no-dev --no-interaction --no-ansi

# プロジェクトファイルをコピー
COPY . /app/

# ポートを公開
EXPOSE 8000

# Gunicornを使用してアプリケーションを起動
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]