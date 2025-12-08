# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        temp1=list1
        temp2=list2
        res=None
        head=None

        if list1==None and list2==None:
            return list1
        elif list1!=None and list2==None:
            return list1
        elif list1==None and list2!=None:
            return list2
        else:
            if temp1.val<=temp2.val:
                res=temp1
                temp1=temp1.next
            else:
                res=temp2
                temp2=temp2.next
            
            head=res
           

            while temp1!=None and temp2!=None:
                if temp1.val<=temp2.val:
                    res.next=temp1
                    temp1=temp1.next
                    res=res.next
                else:
                    res.next=temp2
                    temp2=temp2.next
                    res=res.next
                
            while temp1!=None:
                res.next=temp1
                temp1=temp1.next
                res=res.next

            while temp2!=None:
                res.next=temp2
                temp2=temp2.next
                res=res.next
    
        return head