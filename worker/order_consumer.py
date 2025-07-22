import pika
import json
from pymongo import MongoClient

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='orders')

client = MongoClient('mongodb://mongo:27017/')
db = client['trading_db']
trade_collection = db['trades']

def callback(ch, method, properties, body):
    order = json.loads(body)
    print(f"Processing Order: {order}")
    trade_collection.insert_one(order)

channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)
print('Waiting for orders...')
channel.start_consuming()
