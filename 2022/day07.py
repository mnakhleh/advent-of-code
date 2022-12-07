from data.day07 import SAMPLE_TXT, INPUT_TXT
from anytree import Node, LevelOrderIter
from typing import Iterator


TOTAL_SPACE = 70_000_000
NEEDED_SPACE = 30_000_000


class SizeNode(Node):
    size: int
    typ: str

    def __len__(self) -> int:
        total_size = self.size if self.typ == 'file' else 0
        for child in self.children:
            if child.typ == 'file':
                total_size += child.size
            else:
                total_size += len(child)
        return total_size


def get_file_tree(txt: str) -> SizeNode:
    root = SizeNode('root', typ='dir')
    cur_node = root
    commands = txt.splitlines()[1:]
    for i, command in enumerate(commands):
        if command == '$ cd ..':
            cur_node = cur_node.parent
        elif command == '$ cd /':
            cur_node = root
        elif command.startswith('$ cd'):
            new_node = SizeNode(command[5:], typ='dir', parent=cur_node)
            cur_node = new_node
        elif command == '$ ls':
            j = 0
            while True:
                j += 1
                if len(commands) == i + j:  # Reached end of the list of commands
                    break
                potential_file = commands[i + j]
                if potential_file.startswith('$'):
                    break
                if potential_file.startswith('dir'):
                    continue
                else:
                    size, name = potential_file.split(' ')
                    SizeNode(name, typ='file', size=int(size), parent=cur_node)
    return root


def get_small_dirs(node: SizeNode, threshhold: int) -> Iterator[SizeNode]:
    for node in LevelOrderIter(node):
        if node.typ == 'dir' and len(node) <= threshhold:
            yield node


def part1(txt: str) -> int:
    root = get_file_tree(txt)
    return sum(len(dr) for dr in get_small_dirs(root, 100000))


def part2(txt: str) -> int:
    root = get_file_tree(txt)
    space_to_free = abs(TOTAL_SPACE - NEEDED_SPACE - len(root))

    all_dirs = [len(node) for node in LevelOrderIter(root) if node.typ == 'dir']
    for size in sorted(all_dirs):
        if size >= space_to_free:
            return size


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 95437
    print(part1(INPUT_TXT))
    assert part2(SAMPLE_TXT) == 24933642
    print(part2(INPUT_TXT))

