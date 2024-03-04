from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util

# リクエストボディの定義
class Sentences(BaseModel):
    sentence1: str
    sentence2: str

# FastAPIアプリケーションの初期化
app = FastAPI()

# モデルのロード（事前にダウンロードしておくことで、サーバー起動時の遅延を避ける）
model = SentenceTransformer('stsb-xlm-r-multilingual')

@app.post("/cosine_similarity/")
async def calculate_cosine_similarity(sentences: Sentences):
    # 文章をベクトルに変換
    embeddings1 = model.encode(sentences.sentence1, convert_to_tensor=True)
    embeddings2 = model.encode(sentences.sentence2, convert_to_tensor=True)

    # コサイン類似度の計算
    return util.pytorch_cos_sim(embeddings1, embeddings2)[0][0].item()  # `.item()` で数値を抽出
