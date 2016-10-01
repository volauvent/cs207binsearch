from binsearch import binary_search
from pytest import raises
import numpy as np

def test_bad_input_results():
    with raises(TypeError):
        binary_search([1,2,3,4,5], 2,'a')
    with raises(TypeError):
        binary_search([(1,2),3,4,5], 2)
    with raises(ValueError):
        binary_search([5,4,3,2,1], 2)
    with raises(TypeError):
        binary_search([1,2,3,4,5], 2, 0.5, 1.4)
    with raises(ValueError):
        binary_search([1,2,3,4,5], 2, 1, 100)
        
def test_right_input_results():
    assert binary_search([1,2,3,4,5], 2) == 1
    assert binary_search([], 2) == -1
    assert binary_search(None, 2) == -1
    assert binary_search([1,2,3,4,5], 2) != -1
    assert binary_search([1,2,3,4,5], 6) == -1
    assert binary_search([1,2,3,4,5], 2, 1, 3) == 1
    assert binary_search([1,2,3,4,5], 2, 3, 4) == -1
    assert binary_search([1,2,3,4,5], 2, 3, 4) == -1
    assert binary_search([1,2,3,4,5], 2, 4, 3) == -1
    assert binary_search([1,2,3,np.inf], 2) == 1
    assert binary_search([1,2,3,np.inf], np.inf) == 3
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) == -1

def test_non_num_input_results():
    assert binary_search(['a','b','c'],'b') == 1
    assert binary_search(['a','b','c'],'d') == -1
    assert binary_search("abcd",'b') == 1
    assert binary_search("abcd",'e') == -1