from tkinter import Y


yearly_salaries = [120_000, 72_000, 56_000, 76_000]

# salary_stat = {
#     "count": len(yearly_salaries),
#     "sum": sum(yearly_salaries),
#     "avg": sum(yearly_salaries) / len(yearly_salaries),
# }

# count_salaries = len(yearly_salaries)
# sum_salaries = sum(yearly_salaries)

# salary_stat = {
#     "count": count_salaries,
#     "sum": sum_salaries,
#     "avg": sum_salaries / count_salaries,
# }

# x = 3
# print(x)

# walrus operátor
print(x := 3)

salary_stat = {
    "count": (count_salaries := len(yearly_salaries)),
    "sum": (sum_salaries := sum(yearly_salaries)),
    "avg": sum_salaries / count_salaries,
}

print(salary_stat)
