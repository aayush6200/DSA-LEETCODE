
# algorithm

# # travel through two lists and merge them
# l1 = list1  # for travelling through first node
# l2 = list2  # for travelling through second node

# dummy = ListNode()  # calling the class and creating an instance
# cur = dummy


def merge_linked_list(l1, l2):

    while l1 and l2:
        if l1.val > l2.val:
            cur.next = l2
            l2 = l2.next
        else:
            cur.next = l1
            l1 = l1.next
        cur = cur.next
    if l1:
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
    if l2:
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
    return dummy.next  # returns the head of newly merged linked list

# time complexity: O(m)+O(n) where m is time complexity for  l1 and n is time complexity for l2

# space complexity: O(m)+o(n) where m is space complexity for l1 and n is space complexity
