import pika

def do_nothing(): pass

class RabbitConnection:
    '''
    Class representing connection to RabbitMQ server
    
    Original: https://habr.com/ru/articles/434510/
    '''
    
    def __init__(self, connection_string: str, queue: str):
        self._rmq_params = pika.URLParameters(connection_string)
        self._rmq_conn = pika.BlockingConnection(self._rmq_params)
        self._rmq_channel = self._rmq_conn.channel()
        self.queue = queue
        self._rmq_channel.queue_declare(self.queue, durable=True)
        self._on_receive_callback = do_nothing
        
    def __del__(self):
        self._rmq_conn.close()
        
    def send_message(self, routing: str, body: str) -> None:
        self._rmq_channel.basic_publish(
            exchange='', routing_key=routing, body=body
        )
        
    def set_on_receive_callback(self, callback: function) -> None:
        self._on_receive_callback = callback
        self._rmq_channel.basic_consume(
            queue=self.queue,
            auto_ack=True,
            on_message_callback=self._on_receive_callback,
        )
        
    def get_on_receive_callback(self) -> function:
        return self._on_receive_callback
    
    def run(self) -> None:
        self._rmq_channel.start_consuming()