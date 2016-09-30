
from binsearch import binary_search
from pytest import raises
import numpy as np

def test_notthere():
    assert binary_search([1, 3, 5],2) == -1