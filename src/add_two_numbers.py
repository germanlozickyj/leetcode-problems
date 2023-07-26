
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        numbers = {
            0: [],
            1: []
        }
        
        pointer = 0
        for item in [l1, l2] :
            while(item.next) :
                numbers[pointer].append(item.val)
            pointer+=1
        
        
Solution().addTwoNumbers([2,4,3], [5,6,4])