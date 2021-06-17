'''
we use basic dictionary in this question to make the deep of linked list
'''

def deepcopy(head):
    if not head:
        return None

    curr = head
    dic = {}

    while curr:
        dic[curr] = Node(curr.val,None,None)
        curr = curr.next

    curr = head

    while curr:
        if curr.next:
            dic[curr].next = dic[curr.next]

        if curr.random:
            dic[curr].randome = dic[curr.random]

        curr = curr.next

    return dic[head]