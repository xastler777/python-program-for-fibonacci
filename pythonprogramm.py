def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue for the worker
channel.queue_declare(queue='fibonacci_queue')

# Send input values for the Fibonacci function to the worker
input_values = [10, 100, 56]
for value in input_values:
    message = json.dumps({'input': value})
    channel.basic_publish(exchange='', routing_key='fibonacci_queue', body=message)
    print(f'Sent message: {message}')