import os
import tempfile
import shutil
from src.tree_utils_02.size_node import FileSizeNode
from src.tree_utils_02.size_tree import SizeTree
from src.tree_utils_02.tree import Tree

def test_construct_filenode_file():
    with tempfile.NamedTemporaryFile() as temp_file:
        file_node = FileSizeNode(temp_file.name, is_dir=False, children=[], size=os.path.getsize(temp_file.name))
        assert file_node.size == os.path.getsize(temp_file.name)


def test_update_filenode():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write('Hello, World!')

        tree = SizeTree()
        root_node = tree.get(temp_dir, dirs_only=False)
        updated_root_node = tree.update_filenode(root_node)
        assert updated_root_node.children[0].size == os.path.getsize(file_path)

def test_filter_empty_nodes():
    with tempfile.TemporaryDirectory() as temp_dir:
        tree = Tree()
        file_node = tree.construct_filenode(temp_dir, is_dir=True)
        try:
            tree.filter_empty_nodes(file_node)
        except ValueError as e:
            assert str(e) == 'Code should not be executed here!'

