from simple_library_01.functions import is_leap
import pytest

def test_is_leap():
    with pytest.raises(AttributeError):
            is_leap(0)
            
def test_is_leap1():
    with pytest.raises(AttributeError):
            is_leap(-1)
            
def test_is_leap2():
   assert is_leap(2024)==True
   
   
def test_is_leap2():
   assert is_leap(1930)==False
   
def test_is_leap10():
   assert is_leap(2022)==False
    
def test_is_leap22():
   assert is_leap(1900)==False
   
def test_is_leap3():
   assert is_leap(4)==True
   
def test_is_leap4():
   assert is_leap(100)==False
    
def test_is_leap89():
   assert is_leap(2023)==False
   
def test_is_leap89():
   assert is_leap(400)==True
   
