# 1
roy = [0, 1, 2, 3]
print(list(map(lambda x: x + 10, roy)))

# 2
roy = ["x", "y", "z"]
print(list(map(lambda x: "harf: " + x, roy)))

# 3
roy = [50, 100, 150]
print(list(map(lambda x: x / 2, roy)))

# 4
roy = ["5", "6", "7"]
print(list(map(lambda x: int(x) ** 2, roy)))

# 5
roy = [8, 9, 10]
print(list(map(lambda x: x ** 2, roy)))
