#Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма
#(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#Выведите соответствующее сообщение.
#Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
#Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

plus = float(input('Введите данные по выручке: '))
cost = float(input('Введите данные издержек: '))
if plus > cost:
    print('Ваша компания приносит прибыль. Рентабильность: ', plus / cost)
    employers = int(input('Введите кол-во сотрудников: '))
    print('Прибыль на одного сотрудника: ', plus / employers)
elif plus == cost:
    print('Прибыль и затраты Вашей компании равны')
else:
    print('Ваша компания работает в убыток')
