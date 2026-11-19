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
    pool = Pool(processes=proc_count)
    args = [(i + 1) / 10 for i in range(proc_count)]
    results = pool.map(proc, args)
    pool.close()
    print(results)


if __name__ == "__main__":
    main(160)
