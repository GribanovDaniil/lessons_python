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

    # ������ count(���-�� �����) = 0. ���� � ��� num ������ 0, �� �������� �� �����. ���� num - ������ , �� �� ��� ����� �� 2 � � �������� ���������� count ���������� 1. ���� num - ��������, �� �� �� num �������� 1 , � � count ���������� 1. � � ����� ���������� �������� ���������� count.
    # ��������� - O(log(num))
