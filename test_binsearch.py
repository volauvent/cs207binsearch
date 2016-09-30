from binsearch import binary_search
from pytest import raises
import numpy as np
import amath

def test_notthere():
    assert binary_search([1, 3, 5],2) == -1

def test_there():
    assert binary_search([1, 3, 5],3) == 1

def array_len():
    with raises(ValueError):
        binary_search([],3)
        
def index_len():
    with raises(ValueError):
        binary_search([1,3,5])
    
def int_char():
    with raises(TypeError):
        binary_search([1,3,5,8],3,'a')
    
def int_order():
    with raises(ValueError):
        binary_search([1,3,5,8],3,1)