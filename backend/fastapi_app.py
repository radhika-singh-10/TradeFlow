from fastapi import FastAPI
import redis
import json

app = FastAPI()
redis_client = redis.Redis(host='redis', port=6379)

@app.post("/publish_ltp/")
def publish_ltp(symbol: str, price: float):
    data = {"symbol": symbol, "price": price}
    redis_client.publish('ltp_channel', json.dumps(data))
    return {"status": "published", "data": data}
