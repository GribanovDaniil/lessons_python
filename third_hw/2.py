# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0 
        while head:
            res = res * 2 + head.val
            head = head.next
        return res

#сначала перебираю связнный список, преобразовывая его в 10 систему
#затем беру значение и умножаю его на 2, потом прибавляю значение следующего элмемента и т.д
#сложность О(N)