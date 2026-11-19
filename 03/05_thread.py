from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep


def minion(text):
    sleep(1)
    print(f"Banana! {text}")
    return "Poopaye!"


if __name__ == "__main__":
    with ThreadPoolExecutor() as ex:
        args = ["Gru", "Kevin"]
        futures = [ex.submit(minion, arg) for arg in args]
        print([f.result() for f in as_completed(futures)])
