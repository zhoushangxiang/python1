import pika
#1.
connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()
channel.queue_declare(queue='xxx')
channel.basic_publish(exchange='',routing_key='xxx',body='hello world')
print("[x]Sent'hello world!'")
connection.close()

#2.
connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()
channel.queue_declare(queue='qqq')
channel.basic_publish(exchange='',routing_key='qqq',body='hello kitty')
print("[x]Sent'hello world!'")
connection.close()