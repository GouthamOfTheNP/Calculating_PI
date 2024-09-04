import math

index = 1

while index <= 10**20:
    result = index * math.sin(math.radians(180) / index)
    index += 1
    print(result)
