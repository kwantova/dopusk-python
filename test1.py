from tukey import split_sample

data = [12, 13, 24, 34, 35, 46, 56, 57, 68, 78, 79, 80, 90]
percentiles = [0, 25, 50, 75, 100]

for p in percentiles:
    print(f"{p}-й процентиль: {split_sample(data, p)}")
