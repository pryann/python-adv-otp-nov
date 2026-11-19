from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import Pool, Process
from time import perf_counter, sleep


def performance_meter(fn):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        fn(*args, **kwargs)
        stop = perf_counter()
        print(f"Complete: {stop - start:.4f} sec")

    return wrapper


def proc(delay):
    sleep(delay)
    return "value"


@performance_meter
def main(proc_count):
    with ProcessPoolExecutor() as ex:
        results = [ex.submit(proc, i + 1) for i in range(proc_count)]
        print([i.result() for i in as_completed(results)])


if __name__ == "__main__":
    main(5)
