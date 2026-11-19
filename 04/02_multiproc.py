from multiprocessing import Process
from time import perf_counter, sleep


def performance_meter(fn):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        fn(*args, **kwargs)
        stop = perf_counter()
        print(f"Complete: {stop - start:.4f} sec")

    return wrapper


def proc():
    sleep(1)


@performance_meter
def main(proc_count):
    processes = []
    for _ in range(proc_count):
        p = Process(target=proc)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


if __name__ == "__main__":
    main(160)
