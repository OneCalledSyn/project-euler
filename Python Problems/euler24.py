import math

number = 1000000
answer = ""
l = 10
choices = [x for x in range(l)]

for i in range(l, 0, -1):
    counter = 0

    while True:
        number -= math.factorial(i - 1)
        if number <= 0:
            number += math.factorial(i - 1)
            break
        counter += 1

    answer = answer.join(str(choices[counter]))
    choices.remove(choices[counter])

    print(answer, number)
