package binary_heap

import (
	"errors"
)

type MaxHeap struct {
	heap         []int64
	heapSize     int
	heapCapacity int
}

func NewMaxHeap(capacity int) *MaxHeap {
	return &MaxHeap{
		heap:         make([]int64, capacity),
		heapSize:     0,
		heapCapacity: capacity,
	}
}

func (h *MaxHeap) parent(index int) int {
	return (index - 1) / 2
}

func (h *MaxHeap) left(index int) int {
	return 2*index + 1
}

func (h *MaxHeap) right(index int) int {
	return 2*index + 2
}

func (h *MaxHeap) Insert(key int64) error {
	if h.heapSize == h.heapCapacity {
		return errors.New("can't insert any more keys, max heap tree is already full")
	}

	// increase heap size before insertion
	h.heapSize++

	index := h.heapSize - 1
	h.heap[index] = key

	for index != 0 && h.heap[h.parent(index)] < h.heap[index] {
		h.heap[h.parent(index)], h.heap[index] = h.heap[index], h.heap[h.parent(index)]
		index = h.parent(index)
	}

	return nil
}

func (h *MaxHeap) Get() []int64 {
	return h.heap[0:h.heapSize]
}
