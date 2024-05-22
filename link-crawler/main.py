import worker_library
import os
import httpx

connection = worker_library.RabbitConnection(
    f'ampq://{ os.environ.get('RABBIT_USER') }:' + 
    f'{ os.environ.get('RABBIT_PASS') }@'
    f'{ os.environ.get('RABBIT_HOST') }:' +
    f'{ os.environ.get('RABBIT_PORT') }/',
    'links'
)

def get_link_source(ch, method, properties, body):
    link = body
    response = httpx.get(link)
    
    if response.status_code == 200:
        connection.send_message('pages', response.content.decode('utf-8'))

if __name__ == '__main__':
    connection.run()