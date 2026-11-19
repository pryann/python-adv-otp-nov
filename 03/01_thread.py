from threading import Thread, current_thread
from time import perf_counter, sleep

thread = current_thread()
print(thread)


def task():
    print("start long running I/O task...")
    sleep(2)
    print("end long running I/O task")


if __name__ == "__main__":
    start = perf_counter()
    # task()
    # task()
    t1 = Thread(target=task)
    t2 = Thread(target=task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = perf_counter()
    print(f"Complete: {end - start:.4f} sec.")
