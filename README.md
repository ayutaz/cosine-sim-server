# 文章類似計算をするシンプルサーバー

SentenceTransformerを使った文章の類似度計算をするシンプルなサーバーです。

<!-- TOC -->
* [文章類似計算をするシンプルサーバー](#文章類似計算をするシンプルサーバー)
* [使い方](#使い方)
<!-- TOC -->

# 使い方
1. dockerのビルド
```bash
docker-compose up --build
```

2サーバーにリクエストを送る
```bash
curl -X 'POST' \
  'http://0.0.0.0:8000/cosine_similarity/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sentence1": "string",
  "sentence2": "string"
}'
```

レスポンス
```json
{
  0.9999998807907104
}
```

# ライセンス
Apache License 2.0