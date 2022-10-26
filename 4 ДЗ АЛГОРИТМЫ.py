class Solution(object):
    def sumBase(self, n, k):
        a = ''
        while n > 0:
            a += str(n % k)
            n = n // k
        b = 0
        for i in a:
            b += int(i)
        return b

        # Переводим число n в 10чной системе счисления в k - тую систему счисления. И находим сумму цифр числа n в k - той системе счисления.
        # Сложность - O(logk(n))