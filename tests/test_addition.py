# from src.calculator import add
from src.calculator import add
# from 
import pytest
def test_add():
    result = add(3, 4)
    assert result == 7
def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)
