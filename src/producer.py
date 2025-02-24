import pika

QUEUE_NAME = 'task_queue'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue=QUEUE_NAME, durable=True)

message = "Hello, RabbitMQ!"
channel.basic_publish(exchange='',
                      routing_key=QUEUE_NAME,
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2))

print(f" [x] Sent '{message}'")
connection.close()
