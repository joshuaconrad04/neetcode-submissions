class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val
        self.key = None
        self.prev = None

class LRUCache: 

    def __init__(self, capacity: int):

        self.capacity = capacity
                        #key = key, value = ptr to node in linked list
        self.hash_map = {}
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append_node(self, node):
        prev = self.tail.prev
        self.tail.prev = node
        prev.next = node
        node.prev = prev
        node.next = self.tail

    def delete_node(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]
        self.delete_node(node)
        self.append_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.hash_map:
            node = self.hash_map[key]
            self.delete_node(node)
            node.val = value
            self.append_node(node)
            return
        #full so I need to evict LRU
        if len(self.hash_map) == self.capacity:
            LRU = self.head.next
            print(LRU.val)
            self.delete_node(LRU)
            self.hash_map.pop(LRU.key)

            #now append new node
            new_node = ListNode(value)
            new_node.key = key
            self.hash_map[key]=new_node
            self.append_node(new_node)
        else:
            #if I need add an actual new value

            new_node = ListNode(value)
            new_node.key = key
            self.hash_map[key] = new_node
            self.append_node(new_node)

        










        
