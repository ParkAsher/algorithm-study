class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        
        # index 1 과 맨끝을 교환
        self.items[1], self.items[-1] = self.items[-1], self.items[1]

        # 맨끝으로 이동한 최댓값을 뽑아냄
        max_data = self.items.pop()

        # 맨위로 올라간 맨끝 요소의 인덱스
        cur_index = 1

        # 끝까지 비교
        while cur_index <= len(self.items) - 1 :
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            # 왼쪽 자식이 있다 
            if left_child_index <= len(self.items) -1 and self.items[left_child_index] > self.items[max_index] :
                max_index = left_child_index

            # 오른쪽 자식이 있다.
            if right_child_index <= len(self.items) -1 and self.items[right_child_index] > self.items[max_index] :
                max_index = right_child_index

            # 현재 인덱스가 제일 크다. 교체 x
            if max_index == cur_index:
                break    

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index

        return max_data


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]