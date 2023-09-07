import pytest 
from extract import get_input

# Test that file is read into a list
def test_input_is_list():
    # Arrange
    filename = 'results.csv'
    expected_type = list

    # Act
    output = get_input(filename)

    # Assert
    assert type(output) == expected_type


# Test that file exists