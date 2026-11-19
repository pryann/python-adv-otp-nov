from concurrent.futures import ThreadPoolExecutor
from time import ctime, perf_counter, sleep, time


def log_service(thread_name, delay):
    while is_log:
        sleep(delay)
        print(f"{thread_name}: {ctime(time())}")


if __name__ == "__main__":
    start = perf_counter()
    max_tasks = 5
    is_log = True

    with ThreadPoolExecutor(max_workers=5) as ex:
        args = ((f"Thread-{i + 1}", i + 1) for i in range(max_tasks))
        ex.map(log_service, *zip(*args))
        sleep(10)
        is_log = False

    end = perf_counter()
    print(f"Complete: {end - start:.4f} sec.")
