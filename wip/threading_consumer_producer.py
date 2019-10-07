import time
from queue import Queue
from threading import Thread


def producer_func(queue):
    print(f"Putting {1}")
    queue.put(1)
    print(f"Putting {2}")
    queue.put(2)
    print(f"Producer waiting for more tasks")
    time.sleep(2)
    print(f"Putting {3}")
    queue.put(3)
    print(f"Producer shuting down")
    queue.put(None)


def consumer_func(queue):
    while True:
        task = queue.get()
        if task is None:
            print(f"Got None, exiting")
            queue.task_done()
            break
        time.sleep(0.5)
        queue.task_done()
        print(f"Task Done {task}")

queue = Queue()
producer = Thread(target=producer_func(queue))
consumer = Thread(target=consumer_func(queue))
producer.start()
consumer.start()
queue.join()