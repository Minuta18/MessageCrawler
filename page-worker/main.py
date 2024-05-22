import worker_library
import os
import httpx
import bs4

connection = worker_library.RabbitConnection(
    f'ampq://{ os.environ.get('RABBIT_USER') }:' + 
    f'{ os.environ.get('RABBIT_PASS') }@'
    f'{ os.environ.get('RABBIT_HOST') }:' +
    f'{ os.environ.get('RABBIT_PORT') }/',
    'pages'
)

def get_links_by_source(ch, method, properties, body):
    page = body
    soup = bs4.BeautifulSoup(page, 'html.parser')
    
    for link in soup.find_all('a'):
        connection.send_message('links', link.get('href'))
    
if __name__ == '__main__':
    connection.set_on_receive_callback(get_links_by_source)
    connection.run()