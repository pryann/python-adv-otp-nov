import csv
from os import path


def read_csv(file_path):
    with open(file_path, "r") as f:
        reader = csv.reader(f, delimiter=",")
        return [row for row in reader]


full_path = path.join("06", "survey_results_public.csv")

# print(read_csv(full_path))


def read_csv_gen(file_path):
    with open(file_path, "r") as f:
        yield from f


result = read_csv_gen(full_path)
print(next(result))
print(next(result))
print(next(result))
