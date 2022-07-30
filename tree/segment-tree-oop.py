parent = lambda i: int(i / 2)
left = lambda i: i * 2
right = lambda i: i * 2 + 1


def closest_pow2(n):
    k = 1

    while k < n:
        k <<= 1
    
    return k


class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        self.__list_length = closest_pow2(n)
        self.__list = arr + [0] * (self.__list_length - n)
        self.__tree = self.__build_tree(self.__list)

    def __build_tree(self, arr):
        n = len(arr)
        tree = [0] * 2 * n

        for i in range(n):
            tree[i + n] = arr[i]

        for i in range(n - 1, 0, -1):
            tree[i] = tree[left(i)] + tree[right(i)]

        return tree

    def __query_helper(self, index, lower_bound, upper_bound, query_l, query_r):
        if query_l <= lower_bound and upper_bound <= query_r:
            return self.__tree[index]

        if upper_bound < query_l or query_r < lower_bound:
            return 0

        new_bound = (lower_bound + upper_bound) // 2
        l = self.__query_helper(left(index), lower_bound, new_bound, query_l, query_r)
        r = self.__query_helper(right(index), new_bound + 1, upper_bound, query_l, query_r)

        return l + r

    def query(self, query_l, query_r):
        return self.__query_helper(1, 0, self.__list_length - 1, query_l - 1, query_r - 1)

    def update(self, index, data):
        index = index + self.__list_length
        self.__tree[index] = data

        while index > 1:
            self.__tree[parent(index)] = self.__tree[left(parent(index))] + self.__tree[right(parent(index))]
            index = parent(index)
        
        return self.tree()

    def tree(self):
        return self.__tree


if __name__ == '__main__':
    st = SegmentTree([3, 2, 4, 5, 1, 1, 5, 3])
    assert st.tree() == [0, 24, 14, 10, 5, 9, 2, 8, 3, 2, 4, 5, 1, 1, 5, 3]
    assert st.query(2, 4) == 11
    assert st.query(5, 6) == 2
    assert st.query(1, 8) == 24
    assert st.query(3, 3) == 4

    st = SegmentTree([1, 2, 3, 4, 5])
    assert st.tree() == [0, 15, 10, 5, 3, 7, 5, 0, 1, 2, 3, 4, 5, 0, 0, 0]
    assert st.update(2, 4) == [0, 16, 11, 5, 3, 8, 5, 0, 1, 2, 4, 4, 5, 0, 0, 0]
    assert st.update(3, 99) == [0, 111, 106, 5, 3, 103, 5, 0, 1, 2, 4, 99, 5, 0, 0, 0]
    assert st.query(3, 4) == 103
    assert st.query(1, 8) == 111
