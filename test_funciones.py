"""
Your module description
"""
from funciones import sumar
from funciones import primo
def test_sumar():
    assert sumar(2,4) == 6 
    assert sumar(-2,4) == 2
    assert sumar (2,2) == 4
    
def test_primo():
    assert primo(2) is False
    
    