# sum range segment tree implementation


left = lambda index: index * 2
right = lambda index: index * 2 + 1
parent = lambda index: int(index / 2)
is_odd = lambda num: num % 2 != 0


def to_segment_tree(arr):
    n = len(arr)
    tree = [0] * 2 * n

    for i in range(n):
        tree[n + i] = arr[i]
     
    for i in range(n - 1, 0, -1):
        tree[i] = tree[left(i)] + tree[right(i)]

    return tree


def update(tree, n, index, data):
    index = index + n
    tree[index] = data

    while index > 1:
        tree[parent(index)] = tree[left(parent(index))] + tree[right(parent(index))]
        index = parent(index)

    return tree


def query(tree, n, l, r):
    l += n
    r += n + 1
    result = 0

    while l < r:
        if is_odd(l):
            result += tree[l]
            l += 1

        if is_odd(r):
            r -= 1
            result += tree[r]

        l = parent(l)
        r = parent(r)

    return result 


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    tree = to_segment_tree(arr)

    assert tree == [0, 15, 10, 5, 9, 1, 2, 3, 4, 5]
    assert update(tree, len(arr), 4, 9) == [0, 19, 14, 5, 13, 1, 2, 3, 4, 9]
    assert query(tree, len(arr), 0, 4) == 19
    assert query(tree, len(arr), 3, 4) == 13
