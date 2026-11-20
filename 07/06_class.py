from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def run_query(self):
        pass

    def log(self):
        print("log")


class SQLDatabase(Database):
    def connect(self):
        print("sql connect")

    def close(self):
        print("close")

    def run_query(self):
        print("run")


sqldb = SQLDatabase()
sqldb.run_query()
sqldb.log()
