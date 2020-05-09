# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

### I was waisting a lot of time(at least 40 minutes) in checking if the length of heap is larger than k, but in fact, there is no need. By poping out the heap, the size of the heap will be self-maintained...... 
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return
        k = len(lists)
        heap = []
        dummy = ListNode(0)
        print("##")
        for node in lists:  ### initilze the heap
            if node: heapq.heappush(heap, (node.val, random.random(), node))
        #dummy.next = heap[0][1]
        node = dummy  ### assign the dummy to node, node always at the end of the merged list...... and dummy is used to output the head.....
        while heap:                
            temp = heapq.heappop(heap)  ## there is no need to check the length of heap, because for each node that pop out, only one will pop in, if any one of the list hit the end, the length of the heap will be less than k
            node.next = temp[2]
            node = node.next
            if temp[2].next: 
                next_node = temp[2].next ### need to assign temp[2].next to a pointer, if I do temp[2] = temp[2].next, it will error out
                heapq.heappush(heap, (next_node.val, random.random(), next_node))  ### the second element needs to a number, if I put a node as a second element, there will be error
        return dummy.next
                
