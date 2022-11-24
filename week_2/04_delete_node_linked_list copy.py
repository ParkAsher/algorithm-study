class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):

        node = self.head

        count = 0
        while count < index:
            node = node.next
            count += 1

        return node

    # index 번째에 새로운 노드추가
    def add_node(self, index, value):
        # 새로운 노드
        new_node = Node(value)

        # head 앞에다가 (맨 앞에) 노드를 추가하고싶을때
        if index == 0 :
            new_node.next = self.head   # 새로운 노드의 next에 head를 걸어놓고
            self.head = new_node        # head가 새로운 노드(맨앞) 을 가리키게
            return

        # index번째 노드
        node = self.get_node(index-1)        
        # index번째 노드의 다음거를 미리 저장
        next_node = node.next

        # node - new_node - next_node 형태로 새롭게 연결
        node.next = new_node
        new_node.next = next_node        

        return

    # index 번째 노드 삭제
    def delete_node(self, index) :

        # 0번째 (맨앞노드) 를 삭제하고싶을때
        if index == 0 :
            self.head = self.head.next
            return

        node = self.get_node(index-1)
        node.next = node.next.next
    

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.print_all()

linked_list.delete_node(0)
linked_list.print_all()