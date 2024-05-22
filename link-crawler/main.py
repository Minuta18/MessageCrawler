import worker_library
import os
import httpx
import logging

logging.basicConfig(level=logging.INFO)

connection = worker_library.RabbitConnection(
    f'amqp://{ os.environ.get("RABBIT_USER") }:' + 
    f'{ os.environ.get("RABBIT_PASS") }@'
    f'{ os.environ.get("RABBIT_HOST") }:' +
    f'{ os.environ.get("RABBIT_PORT") }/',
    'links'
)

def get_link_source(ch, method, properties, body):
    logging.info(f'[+] Received message: { body }')
    link = body.decode('utf-8')
    response = httpx.get(link)
    
    if response.status_code in [200, 302]:
        logging.info(
            f'[-] Send message: { response.content.decode("utf-8")[:50] }...'
        )
        connection.send_message('pages', response.content.decode('utf-8'))
    else:
        logging.error(f'[-] { link } returned error: { response.status_code }')

if __name__ == '__main__':
    logging.info('Service started')
    connection.set_on_receive_callback(get_link_source)
    connection.run()