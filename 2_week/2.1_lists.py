...
#---------------------
    2.5 Задача №1
#---------------------
Напишите программу, на вход которой подается одна строка с целыми числами.
Программа должна вывести сумму этих чисел.

Используйте метод split строки.
...

str = [ int(i) for i in input().split()]
summ = 0 
l = len(str)-1
for i in range(0,l + 1):
    summ = summ + str[i]
print(summ)

...
#---------------------
    2.5 Задача №2
#---------------------
Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
ля элементов списка, являющихся крайними, одним из соседей считается элемент,
находящий на противоположном конце этого списка.
Например, если на вход подаётся список "1 3 5 6 10",
то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
...

s = [ int(i) for i in input().split()]
t = []
l = len(s)-1
n = 0
i = 0
if len(s) == 0:
    print(str(0))
else:
    for st in s:
        if len(s) > 1:
            if i == 0:
                n = s[i + 1] + s[-1]
                t.append(n)
            elif i > 0 and i < l:
                n = s[i - 1] + s[i + 1]
                t.append(n)
            elif i == l:
                n = s[i - 1] + s[0]
                t.append(n)
        elif len(s) == 1:
            n = s[i]
            t.append(n)       
        i += 1
    j = 0
    for st2 in t:
        print(str(t[j]) + ' ', end = '')
        j += 1
        
...
#---------------------
    2.5 Задача №3
#---------------------
Напишите программу, которая принимает на вход список чисел в одной строке
и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
...

s = [ int(i) for i in input().split()]
t = []
s.sort()
l = len(s)-1
n = 100000
if len(s)!=1:
    for i in range(0, l):
        if s[i] == s[i + 1] and s[i] != n:
            t.append(s[i])
            n = s[i]
    for j in range(l, l + 1):
        if s[-1] == s[-2] and s[j] != n:
            t.append(s[j])
k = len(t)
for g in range(0, k):
    print(t[g], end = ' ')