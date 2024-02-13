# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Creates integers to hold the numbers stored in the ListNodes
        num1 = 0
        num2 = 0

        # Creates an int to be increased by mutliples of 10 and allow proper addition to the number being created
        mult10 = 1

        # Loops through the first list node to create its stored number
        while l1 != None:
            num1 += l1.val*mult10
            mult10 = mult10*10
            l1 = l1.next
        
        print(num1)
        # Resets mult10 to start creating the second number
        mult10 = 1

        # Loops through the second list node to create its stored number
        while l2 != None:
            num2 += l2.val*mult10
            mult10 = mult10*10
            l2 = l2.next

        # Creates the sum of the two nodes
        numSum = num1+num2
        print(numSum)

        # Creates a Head Node for the return list
        retList = ListNode()
        # Creates the next node in the list and points the head towards it
        nextNode = ListNode()
        retList.next = nextNode

        # Modulus 10 on the sum of numbers, adding them in reverse order to the return list
        for i in range(0,len(str(numSum))):
            nextNode.val = numSum%10
            numSum = int(numSum/10)
            print(nextNode.val)
            # Checks to see if there is another number in the sum to add to the list
            # If not, does not create another node on the list
            if numSum != 0:
                nextNode.next = ListNode()
                nextNode = nextNode.next

        return retList.next


        