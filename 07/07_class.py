from typing import Protocol


class Database(Protocol):
    def connect(self): ...

    def close(self): ...

    def run_query(self): ...


class SQLDatabase(Database):
    def connect(self):
        print("Connect")

    def close(self):
        print("close")

    def run_query(self):
        print("run")


class NoSQLDatabase(Database):
    def connect(self):
        print("Connect")

    def close(self):
        print("close")

    def run_query(self):
        print("run")


def connection(db: Database) -> None:
    db.connect()


connection(SQLDatabase())
connection(NoSQLDatabase())

# sqldb = SQLDatabase()
# sqldb.connect()
