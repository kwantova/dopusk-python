import tukey as t
import alg as a
import graph as g

nums = []
while True:
    try:
        num = float(input("Введите число (любую букву для завершения): "))
    except ValueError:
        print("Ввод окончен.")
        break
    if num == -1: break
    nums.append(num)
try:
    print("Математическое ожидание введенной Вами выборки:", a.custom_mean(nums))
    print("Дисперсия введенной Вами выборки:", a.custom_var(nums))

    print("-----  Данные для диаграммы Тьюки -----")

    lq = t.split_sample(nums, p=25)
    print("Нижний квартиль:", lq)
    median = t.split_sample(nums, p=50)
    print("Медиана:", median)
    uq = t.split_sample(nums, p=75)
    print("Верхний квартиль:", uq)
    uw = a.custom_max(nums)
    print("Верхний ус:", uw)
    lw = a.custom_min(nums)
    print("Нижний ус:", lw)

    ch = input("Отобразить диаграмму Тьюки графически? [y/n]: ")
    if ch == "y" or ch == "Y":
        cleannums = t.anomal_check(nums)
        lqc = t.split_sample(cleannums, p=25)
        medianc = t.split_sample(cleannums, p=50)
        uqc = t.split_sample(cleannums, p=75)
        uwc = a.custom_max(cleannums)
        lwc = a.custom_min(cleannums)
        g.custom_tukey(lwc, lqc, medianc, uqc, uwc)

    elif ch == "n" or ch == "N":
        print("Сеанс завершен.")
    else:
        print("Команда не распознана.")

except Exception as e:
    print(f"При вводе данных произошла ошибка: {e}. Перезапустите программу.")
