# -----------------
# Imports
# -----------------

import pytest
#import ipdb; ipdb.set_trace()
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
    msg = 'c'
    expected_result = '*'
    assert convert.convertion(msg)== expected_result

@pytest.mark.convertion
def test_convertion_one_vowel(convert):
    msg = 'a'
    expected_result = 'a'
    assert convert.convertion(msg)== expected_result

@pytest.mark.convertion
def test_convertion_all_vowels(convert):
    msg = 'aeiouaeiou'
    expected_result = 'aeiouaeiou'
    assert convert.convertion(msg)== expected_result

@pytest.mark.convertion
def test_convertion_all_consonants(convert):
    msg = 'bcdfghjklmpqrtvwxyz'
    expected_result = '*******************'
    assert convert.convertion(msg)== expected_result

@pytest.mark.convertion
def test_convertion_all_blank_spaces(convert):
    msg = ' '
    expected_result = '_'
    assert convert.convertion(msg)== expected_result

