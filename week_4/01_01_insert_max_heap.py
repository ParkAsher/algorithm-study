class MaxHeap:
    def __init__(self):
        # 완전 이진 트리를 배열로
        self.items = [None]

    def insert(self, value):
        
        # 1. 새 값을 맨 끝에 넣는다
        self.items.append(value)

        cur_index = len(self.items) - 1

        # 2. 최 상위 까지 반복
        while cur_index > 1:

            parent_index = cur_index // 2

            # 부모랑 비교
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break;

        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!