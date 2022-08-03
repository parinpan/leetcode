from bisect import bisect, bisect_left, bisect_right
import hashlib


TOTAL_SLOTS = 2 ** 256 - 1


class NodeHasher:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.nodes = []
        self.keys = []

    # id is referred to some particular unique key (most of the case)
    def assign_node(self, id):
        key = self.__hash(id)
        index = bisect_right(self.keys, key) % len(self.keys)
        return self.nodes[index]

    def add_node(self, node):
        if len(self.keys) == self.total_slots:
            raise Exception('could not add more nodes')

        key = self.__hash(node)
        index = bisect(self.keys, key)

        if index > 0 and self.keys[index - 1] == key:
            raise Exception('could not add the node due to colission')
        
        self.nodes.insert(index, node)
        self.keys.insert(index, key)

        return key

    def remove_node(self, node):
        if len(self.keys) == 0:
            raise Exception('could not remove a node if list is empty')

        key = self.__hash(node)
        index = bisect_left(self.keys, key)

        if index >= len(self.keys) or self.keys[index] != key:
            raise Exception('could not remove a node if not exists')

        self.nodes.pop(index)
        self.keys.pop(index)

        return key

    def __hash(self, node):
        hashed = hashlib.sha256(node.encode('utf-8'))
        return int(hashed.hexdigest(), 16) % self.total_slots


if __name__ == '__main__':
    nh = NodeHasher(TOTAL_SLOTS)
    assert nh.add_node('127.0.0.1') == 8498697990858116045933854305162908519226199895615560446064629368736461124000
    assert nh.add_node('127.0.0.2') == 13960538657664721371020229206529537126046542672829607039375399820289283274401
    assert nh.add_node('127.0.0.3') == 11246435625357618822898889593265715599316632898717447629277429676399966941933
    assert nh.add_node('127.0.0.4') == 84535468863624382542614728459539028202349372872620677379179818336676170852492
    assert nh.remove_node('127.0.0.4') == 84535468863624382542614728459539028202349372872620677379179818336676170852492
    assert nh.assign_node('ayam_goreng_fried_chicken_990') == '127.0.0.1'
    assert nh.assign_node('ayam_goreng_fried_chicken_843') == '127.0.0.2'
    assert nh.assign_node('ayam_goreng_fried_chicken_948') == '127.0.0.3'
