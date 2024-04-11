import os
import pytest
import tempfile
import shutil
from src.tree_utils_02.tree import Tree
from src.tree_utils_02.node import FileNode

@pytest.fixture
def temp_dir_with_files():
    temp_dir = tempfile.mkdtemp()
    files = ['file1.txt', 'file2.txt']
    for file in files:
        with open(os.path.join(temp_dir, file), 'w') as f:
            f.write('This is a test file.')
    yield temp_dir
    shutil.rmtree(temp_dir)

@pytest.fixture
def temp_empty_dir():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

def test_get_nonexistent_path():
    tree = Tree()
    with pytest.raises(AttributeError) as e:
        tree.get("/path/does/not/exist", dirs_only=True)
    assert str(e.value) == 'Path not exist'

def test_get_not_directory():
    tree = Tree()
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(AttributeError) as e:
            tree.get(temp_file.name, dirs_only=True)
    assert str(e.value) == 'Path is not directory'


def test_get_recurse_call_true():
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, 'test_file.txt')
    with open(temp_file_path, 'w') as f:
        f.write('Test content')

    tree = Tree()

    result = tree.get(temp_dir, dirs_only=True, recurse_call=True)

   
    assert isinstance(result, FileNode)
    assert result.name == os.path.basename(temp_dir)
    assert result.is_dir == True
    assert len(result.children) == 0

    
def test_get_file_node(temp_dir_with_files):
    tree = Tree()
    file_node = tree.get(temp_dir_with_files, dirs_only=False)
    assert file_node.name == os.path.basename(temp_dir_with_files)
    assert file_node.is_dir == True
    assert len(file_node.children) == 2

def test_construct_filenode(temp_dir_with_files):
    tree = Tree()
    file_node = tree.construct_filenode(temp_dir_with_files, is_dir=True)
    assert file_node.name == os.path.basename(temp_dir_with_files)
    assert file_node.is_dir == True
    assert len(file_node.children) == 0
    
def test_filter_empty_nodes(temp_empty_dir):
    tree = Tree()
    file_node = tree.construct_filenode(temp_empty_dir, is_dir=True)
    with pytest.raises(ValueError) as e:
        tree.filter_empty_nodes(file_node)
    assert str(e.value) == 'Code should not be executed here!'
    assert os.path.exists(temp_empty_dir)

def test_filter_empty_nodes_empty_dir(temp_empty_dir):
    tree = Tree()
    file_node = tree.construct_filenode(temp_empty_dir, is_dir=True)
    with pytest.raises(ValueError) as e:
        tree.filter_empty_nodes(file_node)
    assert str(e.value) == 'Code should not be executed here!'
    assert os.path.exists(temp_empty_dir)

def test_filter_empty_nodes_non_empty_dir(temp_dir_with_files):
    tree = Tree()
    file_node = tree.get(temp_dir_with_files, dirs_only=False)
    tree.filter_empty_nodes(file_node)
    assert os.path.exists(temp_dir_with_files)
    assert len(os.listdir(temp_dir_with_files)) == 2

def test_update_filenode():
    tree = Tree()
    file_node = FileNode(name='test', is_dir=True, children=[])
    updated_file_node = tree.update_filenode(file_node)
    assert updated_file_node == file_node

def test_update_filenode_children():
    parent_node = FileNode(name='parent', is_dir=True, children=[
        FileNode(name='child1', is_dir=False, children=[]),
        FileNode(name='child2', is_dir=True, children=[
            FileNode(name='subchild1', is_dir=False, children=[])
        ])
    ])
    tree = Tree()
    updated_parent_node = tree.update_filenode(parent_node)
    assert updated_parent_node == parent_node
    

def test_filter_empty_nodes_non_root_dir():
    temp_empty_dir = tempfile.mkdtemp()

    try:
        assert os.path.exists(temp_empty_dir)

        tree = Tree()
        
        tree.filter_empty_nodes(FileNode(name='temp', is_dir=True, children=[]), current_path=temp_empty_dir)

       
     
    finally:
        if os.path.exists(temp_empty_dir):
            shutil.rmtree(temp_empty_dir)
        
        
def test_update_filenode_no_children():
    file_node = FileNode(name='test', is_dir=True, children=[])
    tree = Tree()
    updated_file_node = tree.update_filenode(file_node)
    assert updated_file_node == file_node

def test_update_filenode_with_children():
    parent_node = FileNode(name='parent', is_dir=True, children=[
        FileNode(name='child1', is_dir=False, children=[]),
        FileNode(name='child2', is_dir=True, children=[
            FileNode(name='subchild1', is_dir=False, children=[])
        ])
    ])
    tree = Tree()
    updated_parent_node = tree.update_filenode(parent_node)
    assert updated_parent_node == parent_node

def test_update_filenode_with_new_child():
    parent_node = FileNode(name='parent', is_dir=True, children=[
        FileNode(name='child1', is_dir=False, children=[])
    ])
    new_child = FileNode(name='child2', is_dir=True, children=[])
    parent_node.children.append(new_child)
    tree = Tree()
    updated_parent_node = tree.update_filenode(parent_node)
    assert new_child in updated_parent_node.children

def test_update_filenode_without_children():
    file_node = FileNode(name='test', is_dir=True, children=[])
    tree = Tree()
    updated_file_node = tree.update_filenode(file_node)
    assert updated_file_node == file_node

