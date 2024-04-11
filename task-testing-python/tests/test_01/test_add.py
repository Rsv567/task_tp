from simple_library_01.functions import add


def test_add():
    assert 4 == add(2, 2)
    
def test_add2():
    assert 5 == add(3, 2)
    
def test_add3():
    assert 5 == add(2, 3)
    
def test_add4():
    assert 2 == add(-1, 3)
    
def test_add5():
    assert -1 == add(-1, 0)
    
    
def test_add6():
    assert 0 == add(0, 0)
    
    
def test_add6():
    assert 0 == add(-2, 2)
    
def test_add6():
    assert 2 == add(3, -1)
    
def test_add6():
    assert -3 == add(-2, -1)
    
    

    

