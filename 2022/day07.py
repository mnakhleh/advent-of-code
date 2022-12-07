from anytree import Node, LevelOrderIter

from data.day07 import SAMPLE_TXT, INPUT_TXT

TOTAL_SPACE = 70_000_000
NEEDED_SPACE = 30_000_000


def part1(txt: str) -> int:
    root = get_file_tree(txt)
    return sum(get_size(node) for node in LevelOrderIter(root) if get_size(node) <= 100000)


def part2(txt: str) -> int:
    root = get_file_tree(txt)
    space_to_free = abs(TOTAL_SPACE - NEEDED_SPACE - get_size(root))
    dir_sizes = [get_size(node) for node in LevelOrderIter(root)]
    return min(size for size in dir_sizes if size >= space_to_free)


def get_size(node: Node) -> int:
    return node.size + sum(get_size(child) for child in node.children)


def get_file_tree(txt: str) -> Node:
    # Took from bucketz76 the approach of just accumulating file sizes in dirs directly. Love it
    root = Node('root', size=0)
    cur_node = root
    for i, command in enumerate(txt.splitlines()[1:]):
        if command == '$ cd ..':
            cur_node = cur_node.parent
        elif command == '$ cd /':
            cur_node = root
        elif command.startswith('$ cd'):
            new_node = Node(command[5:], size=0, parent=cur_node)
            cur_node = new_node
        elif command.startswith(('$ ls', 'dir')):
            continue
        else:  # File size
            file_size = int(command.split(' ')[0])
            cur_node.size += file_size
    return root


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 95437
    print(part1(INPUT_TXT))
    assert part2(SAMPLE_TXT) == 24933642
    print(part2(INPUT_TXT))
