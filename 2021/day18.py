from anytree import Node, LevelOrderGroupIter, RenderTree, PreOrderIter
from anytree.exporter import DictExporter
from collections import OrderedDict
import copy


class SN:
    def __init__(self, as_num=None, autoresolve=True):
        self._tree = tree(as_num) if as_num else None
        if autoresolve:
            self.resolve()

    @property
    def magnitude(self):
        root = copy.deepcopy(self._tree)
        for node in self.leaf_to_root(root):
            if len(node.children) != 2:
                continue
            elif all(str(subn.data).isnumeric() for subn in node.children):
                node.data = node.children[0].data*3 + node.children[1].data*2
                node.children = []
        return root.children[0].data

    def __str__(self):
        return '\n'.join(f"{pre}{node.data if node.data is not None else ''}"
                         for pre, _, node in RenderTree(self._tree))

    def __add__(self, other):
        new_sn = SN(autoresolve=False)
        root = Node(None, data=None, children=[self._tree.children[0], other._tree.children[0]])
        new_sn._tree = Node(Node, data=None, children=[root])
        new_sn.resolve()
        return new_sn

    def __eq__(self, other):
        try:
            return self.magnitude == other.magnitude
        except AttributeError:  # Maybe raw int?
            return self.magnitude == int(other)


    def resolve(self):
        while 1:
            explodable = self.explode()
            splittable = self.split()
            if not explodable and not splittable:
                return

    def split(self):
        if all(node.data is None or node.data < 10 for node in PreOrderIter(self._tree)):
            return False
        while 1:
            split = False
            for node in PreOrderIter(self._tree):
                if not node.data:
                    continue
                elif node.data < 10:
                    continue
                # print(f"Checking {node.name} ({node.data}): (subnodes = {[f.data for f in node.children]}")
                # print(str(self) + '\n')
                Node(0, node, data=node.data // 2)
                Node(0, node, data=-(node.data // -2))
                node.data = None
                split = True
                break
            print("Split result")
            print(self)
            if not split:
                return True

    def explode(self):
        if len(list(LevelOrderGroupIter(self._tree))) < 7:
            return False
        while 1:
            last_with_data = None
            carrying_digit = None
            exploded = False
            for node in PreOrderIter(self._tree):
                # print(f"On node {node.data}")
                if not node.parent:
                    continue
                elif node.depth >= 6 and not exploded and node.data is not None and not node.children:
                    exploded = True
                    node_second_digit = node.parent.children[1]
                    carrying_digit = node_second_digit.data
                    if last_with_data:
                        # print(f"On node {node.data}, last with data = {last_with_data.data}")
                        last_with_data.data += node.data
                    node.parent.data = 0
                    node.parent.children = []
                elif node.data is not None:
                    last_with_data = node
                    if carrying_digit is None:
                        continue
                    node.data += carrying_digit
                    carrying_digit = None
            print("Explode result")
            print(self)
            if not exploded:
                return True

    def leaf_to_root(self, root):
        for level in reversed(list(LevelOrderGroupIter(root))):
            for node in level:
                yield node


def tree(snail_number):
    main_tree = Node('0', data=None)
    tree_queue = [main_tree]
    node_count = 1
    for i, char in enumerate(str(snail_number)):
        if char == ' ':
            continue
        elif char == '[':
            tree_queue.append(Node(node_count, data=None, parent=tree_queue[-1]))
            node_count += 1
        elif char == ']':
            tree_queue.pop()
        elif char == ',' and str(snail_number)[i+1] != '[':  # So next item is 2nd number, append to node
            tree_queue.pop()
        else:
            if str(snail_number)[i-1].isnumeric():
                continue
            data = int(char + str(snail_number)[i+1]) if str(snail_number)[i+1].isnumeric() else int(char)
            tree_queue.append(Node(node_count, data=data, parent=tree_queue[-1]))
            node_count += 1
    return main_tree


def test():
    # assert SN([9,1]) == 29
    # assert SN([[9,1],[1,9]]) == 129
    # assert SN([[1,2],[[3,4],5]]) == 143
    # assert SN([[[[0,7],4],[[7,8],[6,0]]],[8,1]]) == 1384
    # assert SN([[[[1,1],[2,2]],[3,3]],[4,4]]) == 445
    # assert SN([[[[3,0],[5,3]],[4,4]],[5,5]]) == 791
    # assert SN([[[[5,0],[7,4]],[5,5]],[6,6]]) == 1137
    # assert SN([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488
    # assert (SN([1,2]) + SN([[3,4],5])) == SN([[1,2],[[3,4],5]])
    # assert SN([[6, [5, [4, [3, 2]]]], 1]) == SN([[6, [5, [7, 0]]], 3])
    # assert SN([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]) == SN([[3,[2,[8,0]]],[9,[5,[7,0]]]])
    # assert (SN([[[[4,3],4],4],[7,[[8,4],9]]]) + SN([1,1])) == SN([[[[0,7],4],[[7,8],[6,0]]],[8,1]])
    # assert (SN([1,1]) + SN([2,2]) + SN([3,3]) + SN([4,4]) + SN([5,5])) == SN([[[[3,0],[5,3]],[4,4]],[5,5]])
    assert (SN([1,1]) + SN([2,2]) + SN([3,3]) + SN([4,4]) + SN([5,5]) + SN([6,6])) == SN([[[[5,0],[7,4]],[5,5]],[6,6]])

    assert (SN([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]) + SN([7,[[[3,7],[4,3]],[[6,3],[8,8]]]])
            == SN([[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]))
    # print(sn_actual)
    # assert sn_add.magnitude == sn_actual.magnitude



##########################
if __name__ == '__main__':
    test()

