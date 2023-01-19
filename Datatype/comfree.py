numList01 = []
for num in range(1, 6) :
    numList01.append(num)
print(numList01)

numList02 = [num * num for num in range(1, 6)]
print(numList02)

numList03 = [num for num in range(1, 21) if num % 3 == 0]
print(numList03)