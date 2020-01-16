import pika

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

channel.queue_declare(queue='qqq')
        #Terminal: sudo rabbitmqctl list_queues

def callback(ch,method,properties,body):
    print("[x] Received %r"%body)
channel.basic_consume(queue='qqq',auto_ack=True,on_message_callback=callback)

print('[*]Waiting for messages.To exit press CTRL+C')
channel.start_consuming()