from anytree import Node, LevelOrderIter

from data.day07 import SAMPLE_TXT, INPUT_TXT

TOTAL_SPACE = 70_000_000
NEEDED_SPACE = 30_000_000


def part1(txt: str) -> int:
    root = get_file_tree(txt)
    return sum(len(node) for node in LevelOrderIter(root) if len(node) <= 100000)


def part2(txt: str) -> int:
    root = get_file_tree(txt)
    space_to_free = abs(TOTAL_SPACE - NEEDED_SPACE - len(root))

    dir_sizes = [len(node) for node in LevelOrderIter(root)]

    # Taken from bucketz76. Love it
    return min(size for size in dir_sizes if size >= space_to_free)


class SizeNode(Node):
    size: int

    def __len__(self) -> int:
        return self.size + sum(len(child) for child in self.children)


def get_file_tree(txt: str) -> SizeNode:
    root = SizeNode('root', size=0)
    cur_node = root
    commands = txt.splitlines()[1:]
    for i, command in enumerate(commands):
        if command == '$ cd ..':
            cur_node = cur_node.parent
        elif command == '$ cd /':
            cur_node = root
        elif command.startswith('$ cd'):
            new_node = SizeNode(command[5:], size=0, parent=cur_node)
            cur_node = new_node
        elif command == '$ ls':
            continue
        elif command.startswith('dir'):
            continue
        else:  # File size
            size = command.split(' ')[0]
            cur_node.size += int(size)
    return root


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 95437
    print(part1(INPUT_TXT))
    assert part2(SAMPLE_TXT) == 24933642
    print(part2(INPUT_TXT))
