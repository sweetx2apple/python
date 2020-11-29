#Узнайте у пользователя число n.
#Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3.
#Считаем 3 + 33 + 333 = 369

n = int(input('Введите любое число n для подсчета в формате n+nn+nnn: '))
num = str(n)
nn = num + num
nnn = num + num + num
result = n + int(nn) + int(nnn)
print('Ответ:',result)


