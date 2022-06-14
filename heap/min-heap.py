def parent(index):
    return int(index - 1 / 2)


def left(index):
    return index * 2 + 1


def right(index):
    return index * 2 + 2


def insert(heap, data):
    heap.append(data)
    current = len(heap) - 1

    while heap[current] < heap[parent(current)]:
        heap[current], heap[parent(current)] = heap[parent(current)], heap[current]
        current = parent(current)


def heapify(heap, index):
    while left(index) < len(heap):
        smallest_index = left(index)

        if right(index) < len(heap) and heap[right(index)] < heap[left(index)]:
            smallest_index = right(index)

        if heap[smallest_index] < heap[index]:
            heap[smallest_index], heap[index] = heap[index], heap[smallest_index]

        index = smallest_index


def pop(heap):
    if len(heap) == 0:
        return heap[0]

    top = heap[0]
    heap[0] = heap.pop()
    heapify(heap, 0)
    
    return top


if __name__ == '__main__':
    heap = []
    insert(heap, 9)
    insert(heap, 7)
    insert(heap, 3)
    insert(heap, 5)
    insert(heap, 6)
    insert(heap, 0)

    assert heap == [0, 3, 5, 6, 7, 9]
    assert pop(heap) == 0
