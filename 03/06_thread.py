from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from time import sleep

account_balance = 1000


def update_money(lock, transaction, amount):
    global account_balance

    with lock:
        account_balance_copy = account_balance
        account_balance_copy += amount
        sleep(1)
        account_balance = account_balance_copy
    print(f"transaction: {transaction} end, balance:  {account_balance}")


if __name__ == "__main__":
    lock = Lock()
    transactions = [("deposit", 500), ("withdraw", -300)]
    with ThreadPoolExecutor(max_workers=2) as ex:
        for transaction, amount in transactions:
            ex.submit(update_money, lock, transaction, amount)
