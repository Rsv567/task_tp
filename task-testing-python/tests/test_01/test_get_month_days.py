from simple_library_01.functions import get_month_days
import pytest

def test_get_month_days():
    assert get_month_days(2024,2) == 29

def test_get_month_days1():
    assert get_month_days(2023,2) == 28
            

def test_get_month_days2():
   assert get_month_days(1930, 1)==30
   
   
def test_get_month_days3():
 with pytest.raises(AttributeError):
    get_month_days(190, 13)
   
   
def test_get_month_days4():
  with pytest.raises(AttributeError):
    get_month_days(190, -1)
   
   
def test_get_month_days7():
  with pytest.raises(AttributeError):
    get_month_days(190, 0)
   
def test_get_month_days90():
   assert get_month_days(19, 4)==30
   
def test_get_month_days95():
   assert get_month_days(19, 11)==30
   
   
   
def test_get_month_days8():
   assert get_month_days(19, 3)==31
   
   
def test_get_month_days790():
  
    assert get_month_days(1930, 13) ==30
    
def test_get_month_days791(): 
    assert get_month_days(1930, 0) ==30
   
def test_get_month_days93():
   assert get_month_days(19, 6)==30
   
def test_get_month_days99():
   assert get_month_days(19, 9)==30
   
def test_get_month_days134():
   assert get_month_days(19, 4)==30
   
   
   
def test_get_month_days789():
  
    assert get_month_days(1931, 12) ==31
    
def test_get_month_days7923(): 
    assert get_month_days(1931, 1) ==31
