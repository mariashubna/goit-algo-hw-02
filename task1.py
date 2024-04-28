from queue import Queue

queue = Queue()
number = 0

def generate_request():
    global number
    new_application = 'Application'
    queue.put(new_application)
    number += 1
    print(f'Нова заявка {number} додана до черги')

def process_request():
    if not queue.empty():
        queue.get()
        print('Заявка видалена')
    else:
        print('Черга пуста')

while True:
    generate_request()
    process_request()