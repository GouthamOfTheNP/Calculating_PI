import math

index = 1

while True:
    result = index * math.sin(math.radians(180) / index)
    if index >= 10**20:
        break
    index += 1
    print(result)