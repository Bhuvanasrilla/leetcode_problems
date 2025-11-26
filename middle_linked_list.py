import single_linked_list as sll

def middle_linked_list(head,n):
    p=head
    q=head
    if n%2==0:
        while q!=None:
            q=q.next.next
            p=p.next
        return p
    else:
        while q.next!=None:
            q=q.next.next
            p=p.next
        return p


single=sll.LinkedList()
single.append(10)
single.append(20)
single.append(30)
single.append(40)
single.append(50)
single.append(60)
single.printlist()

print(middle_linked_list(single.head,single.length).data)
