class Node :
    # data, next
    def __init__(self, data) :
        self.data = data
        self.next = None


node = Node(3)

first_node = Node(4)

node.next = first_node

"""
print(node.next)
print(node.next.data)
"""

class LinkedList:
    # head만 가지고 있으면 된다.
    def __init__(self, data) :
        self.head = Node(data)

    def append(self, data) :
        
        # head가 None일 때
        if self.head is None:
            # 노드를 생성해서 바로 붙여준다.
            self.head = Node(data)
            return

        # head가 None이 아닐때
        cur = self.head                     # cur 은 head를 가리킨다
        while cur.next is not None:         # 조건 : 다음노드가 없을때까지 반복
            cur = cur.next                  # cur 을 다음노드를 가리키게 한다.
            print("cur is ", cur.data)      
        cur.next = Node(data)               # 다음노드가없다면(맨끝노드) 
                                            # node를 생성해서 붙인다.
        
    def print_all(self) :

        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next



# [3] -> [4] -> [5] -> [6] -> None



linked_list = LinkedList(3)

linked_list.append(4)
linked_list.append(5)

linked_list.print_all()