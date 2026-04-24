#Exercício 1

import time

for num1 in range(5):
    print("Tabuada do ", num1)
    for num2 in range(11):
        print(num1, "x", num2, " = ", num1 * num2)
    time.sleep(3)