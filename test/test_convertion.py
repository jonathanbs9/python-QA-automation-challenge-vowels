# -----------------
# Imports
# -----------------

import pytest
from challenge.challenge import Challenge

# ---------------------------------
# Fixture
# ---------------------------------

@pytest.fixture
def convert():
    return Challenge()
    

# ---------------------------------
# Tests (AAA = Arrange Act Assert)
# ---------------------------------
@pytest.mark.convertion
def test_convertion_one_consonant(convert):
    msg = list('c')
    expected_result = list('*')
    assert convert.convertion(msg)== expected_result

@pytest.mark.convertion
def test_convertion_one_vowel(convert):
    msg = list('a')
    expected_result = list('a')  
    assert convert.convertion(msg)== expected_result

@pytest.mark.convertion
def test_convertion_all_vowels(convert):
    msg = list('aeiouaeiou')
    expected_result = list('aeiouaeiou')  
    assert convert.convertion(msg)== expected_result

@pytest.mark.convertion
def test_convertion_all_consonants(convert):
    msg = list('bcdfghjklmpqrtvwxyz')
    expected_result = list('*******************')  
    assert convert.convertion(msg)== expected_result

@pytest.mark.convertion
def test_convertion_all_blank_spaces(convert):
    msg = list(' ')
    expected_result = list('_')  
    assert convert.convertion(msg)== expected_result

