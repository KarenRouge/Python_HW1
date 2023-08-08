#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
import random
n = int(input())
k = 0
j = 0
for i in range(n):
        coin = random.randint(0, 1)
        if coin == 0:
                k += 1
        else:
                j += 1
print(k if k<n/2 else n-j)

#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

n1 = random.randint(0, 1000)
n2 = random.randint(0, 1000)
c = 0
res = [] + [n1, n2]
for i1 in range(n1 + n2):
    if i == (n1 * i1 - n2)**0.5:
        res.append(i1)
print(*res if len(res) == 2 else res + res)

#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = random.randint(0,1000)
i2 = 1
mult = 2
while mult <= number:
    for i2 in range(0, 1000):
        mult = 2 * i2
        i2 += 1
print(mult)