import sys
sys.path.append(r"python-workspace\src")
import pytest
from colour_code import ColourCode
from word import Importance
from io import StringIO
from unittest.mock import patch

@pytest.fixture
def color_combinations():
    return [
        (True, Importance.HIGH, ColourCode.GREEN),
        (True, Importance.MEDIUM, ColourCode.YELLOW),
        (True, Importance.LOW, ColourCode.YELLOW),
        (False, Importance.HIGH, ColourCode.RED),
        (False, Importance.MEDIUM, ColourCode.GREY),
        (False, Importance.LOW, ColourCode.GREY)
    ]

def test_color_selection(color_combinations):
    for is_matched, importance, expected_color in color_combinations:
        color = ColourCode(is_matched, importance)
        assert color.colour == expected_color

def test_print():
    color = ColourCode(True, Importance.HIGH)
    test_text = "Test"
    expected_output = f"{ColourCode.GREEN}{test_text}{ColourCode.RESET}\n"
    
    with patch('sys.stdout', new=StringIO()) as fake_output:
        color.print(test_text)
        assert fake_output.getvalue() == expected_output

def test_print_no_newline():
    color = ColourCode(True, Importance.HIGH)
    test_text = "Test"
    expected_output = f"{ColourCode.GREEN}{test_text}{ColourCode.RESET}"
    
    with patch('sys.stdout', new=StringIO()) as fake_output:
        color.print(test_text, end="")
        assert fake_output.getvalue() == expected_output

def test_str_representation():
    test_cases = [
        (True, Importance.HIGH, "Matched HIGH importance word"),
        (False, Importance.LOW, "Unmatched LOW importance word"),
        (True, Importance.MEDIUM, "Matched MEDIUM importance word")
    ]
    
    for is_matched, importance, expected in test_cases:
        color = ColourCode(is_matched, importance)
        assert str(color) == expected