# 🚀 TradeFlowX

A scalable, containerized trading bot ecosystem built using **Python, FastAPI, Flask, RabbitMQ, Redis Pub/Sub, MongoDB, Docker Compose**, and **Streamlit**.

TradeFlowX enables real-time LTP (Last Traded Price) streaming, concurrent execution of multiple trading algorithms, and order processing using message queues with performance monitoring via a live dashboard.

---

## 📦 Features

- 🏎️ **FastAPI** backend to stream real-time price updates (LTP).
- 🛒 **RabbitMQ** queues for robust order placement and processing.
- 🔁 **Redis Pub/Sub** for real-time market data streaming.
- 💾 **MongoDB** for archiving trades and price history.
- 📊 **Streamlit dashboard** for live performance monitoring.
- 🐳 **Docker Compose** for container orchestration across all services.
- ⚙️ Supports running **multiple trading algorithms** concurrently.

---

## 📐 Architecture Overview

```plaintext
[ Market Price API (FastAPI) ]
          │
          ▼
   [ Redis Pub/Sub ]   ─────────────► (Your Trading Bots / Subscribers)
          │
          ▼
    [ RabbitMQ Queue ] ◄── [ Order Placement (Flask API) ]
          │
          ▼
[ Order Worker / Processor ] ──► [ MongoDB ]
          │
          ▼
[ Streamlit Dashboard ]
```

---

## ⚙️ Project Setup Steps


## 🔥 Method 1: Docker Deployment (Recommended)


```bash
git clone https://github.com/your-username/TradeFlowX.git
```
```bash
cd TradeFlowX
```
```bash
docker-compose up --build
```

## Access Services:

- FastAPI Docs (LTP Streaming): http://localhost:8000/docs

- RabbitMQ Dashboard: http://localhost:15672  (Login: guest / guest)

- Streamlit Dashboard: http://localhost:8501

## 🛠️ Method 2: Local Development (Optional) 

- Requires Python 3.9+, MongoDB, RabbitMQ, and Redis installed locally.

## Set up Python virtual environment:

```bash
python3 -m venv venv
```
```bash 
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
## Start Services Individually:

- FastAPI Backend:

```bash
uvicorn backend.fastapi_app:app --host 0.0.0.0 --port 8000 --reload
```

- Flask Order API (Optional):

```bash
python backend/flask_orders.py
```
- Order Consumer Worker:

```bash
python worker/order_consumer.py
```

- Streamlit Dashboard:

```bash
streamlit run dashboard/dashboard.py
```

- Note: Ensure MongoDB, Redis, and RabbitMQ are running locally on default ports.
