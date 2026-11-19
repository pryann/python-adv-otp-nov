from threading import Thread
from time import ctime, perf_counter, sleep, time


def log_service(thread_name, delay):
    while True:
        sleep(delay)
        print(f"{thread_name}: {ctime(time())}")


if __name__ == "__main__":
    start = perf_counter()
    Thread(target=log_service, args=("Thread-1", 1.1), daemon=True).start()
    Thread(target=log_service, args=("Thread-2", 3), daemon=True).start()
    print("Do other staff")
    sleep(10)
    end = perf_counter()
    print(f"Complete: {end - start:.4f} sec.")
