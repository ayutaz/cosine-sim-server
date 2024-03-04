# Python 3.11のベースイメージを指定
FROM python:3.11

# 作業ディレクトリの設定
WORKDIR /app

# 必要なPythonライブラリをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコンテナにコピー
COPY . .

# デフォルトコマンドの設定
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
