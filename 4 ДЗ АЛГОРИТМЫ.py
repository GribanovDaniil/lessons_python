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

        # ��������� ����� n � 10���� ������� ��������� � k - ��� ������� ���������. � ������� ����� ���� ����� n � k - ��� ������� ���������.
        # ��������� - O(logk(n))