from src.heap import MinHeap, heapsort
import pytest


# Test MinHeap extract_min functionality
def test_extract_min():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    assert heap.extract_min() == 3
    assert heap.extract_min() == 5
    assert heap.extract_min() == 7
    assert heap.extract_min() is None


# Test MinHeap insert functionality
def test_insert():
    heap = MinHeap()
    assert len(heap.heap) == 0
    heap.insert(5)
    assert len(heap.heap) == 1
    heap.insert(3)
    heap.insert(7)
    assert len(heap.heap) == 3


# Test get_min functionality
def test_get_min():
    heap = MinHeap()
    assert heap.get_min() is None
    heap.insert(5)
    assert heap.get_min() == 5
    heap.insert(3)
    heap.insert(7)
    assert heap.get_min() == 3


# Test update functionality
def test_update():
    heap = MinHeap([5, 3, 7, 2, 8])
    heap.update(3, 1)
    assert heap.extract_min() == 1
    heap.update(7, 10)
    assert heap.extract_min() == 2
    assert heap.extract_min() == 5
    assert heap.extract_min() == 8
    assert heap.extract_min() == 10


# Test heapsort
@pytest.mark.parametrize("input_value, expected_output", [
    ([], []),
    ([3], [3]),
    ([6, 2, 8, 1, 4], [1, 2, 4, 6, 8])
])
def test_heapsort(input_value, expected_output):
    result = heapsort(input_value)
    assert result == expected_output


def test_siftup_min_heap_insert():
    min_heap = MinHeap()
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(7)
    min_heap.insert(2)
    min_heap.insert(8)

    # After insertions, the heap should be [2, 3, 7, 5, 8]
    assert min_heap.heap == [2, 3, 7, 5, 8]


def test_siftdown_min_heap_extract():
    min_heap = MinHeap()
    min_heap.heap = [2, 3, 7, 5, 8]
    extracted = min_heap.extract_min()
    # After extraction, the heap should be [3, 5, 7, 8]
    assert min_heap.heap == [3, 5, 7, 8]
    assert extracted == 2


def test_siftup_min_heap_update():
    min_heap = MinHeap()
    min_heap.heap = [2, 3, 7, 5, 8]
    min_heap.update_by_index(2, 1)
    # After update, the heap should be [1, 3, 2, 5, 8]
    assert min_heap.heap == [1, 3, 2, 5, 8]


def test_siftdown_min_heap_update():
    min_heap = MinHeap()
    min_heap.heap = [3, 5, 7, 8, 10]
    min_heap.update_by_index(0, 1)
    # After update, the heap should be [1, 5, 7, 8, 10]
    assert min_heap.heap == [1, 5, 7, 8, 10]
