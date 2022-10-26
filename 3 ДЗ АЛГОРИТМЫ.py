class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        return count

        # Алгоритм проходится по элементам stones и проверяет есть ли этот элемент в jewels. Если есть - к count прибавляем 1. И в конце возвращаем count.
    # Сложность - O(len(stones))