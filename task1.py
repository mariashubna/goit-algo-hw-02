from queue import Queue

queue = Queue()

def generate_request():
    new_application = 'Application'
    queue.put(new_application)
    print('Нова заявка додана до черги')

def process_request():
    if not queue.empty():
        queue.get()
        print('Заявка видалена')
        generate_request()
    else:
        print('Черга пуста')

while True:
    generate_request()
    process_request()
