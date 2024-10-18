"""Тестовое задание - написать программу на python 3.xx (любая 3 версия) которая выводит на экран данные необходимые для построения 
диаграммы Тьюки (Ящик с усами), оценку математического ожидания, дисперсии. Запрещается использовать любые сторонние модули для расчёта
значений. Так же запрещается использовать встроенные функции сортировки, фильтрации, поиска максимума и минимума. Результатом работы 
должны быть 7 чисел (положение конца левого уса, левая граница ящика, медиана, правая граница ящика, конец правого уса, оценка 
математического ожидания и оценка дисперсии). """

import tukey as t
import alg as a
import graph as g

nums = []
while True:
    num = int(input("Введите число (-1 для завершения): "))
    if num == -1: break
    nums.append(num)

print("Математическое ожидание введенной Вами выборки:", a.custom_mean(nums))
print("Дисперсия введенной Вами выборки:", a.custom_var(nums))

print("-----  Данные для диаграммы Тьюки -----")

lq = t.split_sample(nums, p = 25)
print("Нижний квартиль:", lq)
median = t.split_sample(nums, p = 50)
print("Медиана:", median)
uq = t.split_sample(nums, p = 75)
print("Верхний квартиль:", uq)
uw = a.custom_max(nums)
print("Верхний ус:", uw)
lw = a.custom_min(nums)
print("Нижний ус:", lw)

ch = input("Отобразить диаграмму Тьюки графически? [y/n]: ")
if ch == "y" or ch == "Y":
    cleannums = t.anomal_check(nums)
    lqc = t.split_sample(cleannums, p = 25)
    medianc = t.split_sample(cleannums, p = 50)
    uqc = t.split_sample(cleannums, p = 75)
    uwc = a.custom_max(cleannums)
    lwc = a.custom_min(cleannums)
    g.custom_tukey(lwc, lqc, medianc, uqc, uwc)

elif ch == "n" or ch == "N":
    print("Сеанс завершен.")
else:
    print ("Команда не распознана.")