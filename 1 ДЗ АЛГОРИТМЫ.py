class Solution(object):
    def numberOfSteps(self, num):
        count = 0
        while num > 0:
            if (num % 2 == 0):
                num = num / 2
                count = count + 1
            elif (num % 2 != 0):
                num = num - 1
                count = count + 1
        return (count)

    # «адаем count(кол-во шагов) = 0. ѕока у нас num больше 0, мы проходим по циклу. ≈сли num - четное , то мы его делим на 2 и к значению переменной count прибавл€ем 1. ≈сли num - нечетное, то мы от num отнимаем 1 , а к count прибавл€ем 1. » в конце возвращаем значение переменной count.
    # —ложность - O(log(num))
