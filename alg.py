import random

def quicksort(nums):
   """Рекурсивная быстрая сортировка"""
   if not nums: return []
   if len(nums) <= 1: return nums #Крайний случай рекурсии
   else:
       border = random.choice(nums)
       left = []
       middle = []
       right = []
       for n in nums:
           if n < border: left.append(n)
           elif n > border: right.append(n)
           else: middle.append(n)
       return quicksort(left) + middle + quicksort(right)
   
def custom_max(nums):
    """Возвращает максимальное значение непустой коллекции"""
    if not nums: return None
    curmax = nums[0]
    for n in nums[1:]:
        if n > curmax: curmax = n
    return curmax

def custom_min(nums):
    """Возвращает минимальное значение непустой коллекции"""
    if not nums: return None
    curmin = nums[0]
    for n in nums[1:]:
        if n < curmin: curmin = n
    return curmin

def custom_mean(nums):
    """Возвращает математическое ожидание выборки"""
    if not nums: return None
    return sum(nums)/len(nums)

def custom_var(nums):
    """Возвращает дисперсию выборки"""
    if not nums: return None
    sq_dif = [(n - custom_mean(nums)) ** 2 for n in nums]
    return sum(sq_dif) / (len(nums))