from threading import Thread, current_thread
from time import perf_counter, sleep

thread = current_thread()
print(thread)


def task():
    sleep(1)


if __name__ == "__main__":
    start = perf_counter()
    # task()
    # task()
    threads = []
    for i in range(100_000):
        thread = Thread(target=task)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = perf_counter()
    print(f"Complete: {end - start:.4f} sec.")
