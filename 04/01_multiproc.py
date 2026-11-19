from multiprocessing import Process
from time import perf_counter, sleep


def proc():
    sleep(1)


if __name__ == "__main__":
    start = perf_counter()
    p1 = Process(target=proc)
    p2 = Process(target=proc)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    stop = perf_counter()
    print(f"Complete: {stop - start:.4f} sec")
