# Import the functions you want to test

import pytest 
import os
import csv
from extract import *

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

def test_remove_duplicates():
    #Arrange
    test_array = [[4,"Harding","Estrada","no",14],[5,"India","Gentry","yes",7],
                  [6,"Abra","Sheppard","yes",6],[6,"Abra","Sheppard","no",8]]
    #Act
    array_deduped = remove_duplicates(test_array)
    #Assert
    assert array_deduped == [[4,"Harding","Estrada","no",14],[5,"India","Gentry","yes",7],
                  [6,"Abra","Sheppard","yes",6]]

def test_remove_duplicates_from_results():
    #Arrange
    filename = 'results.csv'
    input = get_input(filename) 
    #Act
    array_deduped = remove_duplicates(input)
    #Assert
    assert array_deduped == [['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'], ['1', 'Charissa', 'Clark', 'yes', 'c', '7'], ['2', 'richard', 'McKinney', 'yes', 'b', '7'], ['', '', '', '', '', ''], ['3', 'patience', 'reeves', 'yes', 'b', '9'], ['4', 'Harding', 'Estrada', 'no', 'b', '14'], ['5', 'India', 'Gentry', 'yes', 'c', '7'], ['6', 'Abra', 'Sheppard', 'yes', 'b', '6'], ['7', 'Bryar', 'cooley', 'yes', 'a', '11'], ['8', 'Diana', 'Cameron', 'yes', 'b', '9'], ['9', 'Alexander', 'Herring', 'no', 'b', '4'], ['10', 'Graiden', 'Cannon', 'no', 'b', '13'], ['11', 'Uma', 'Glass', 'yes', 'a', '2'], ['12', 'Brittany', 'Weeks', 'yes', 'b', '8'], ['13', 'Roth', 'Stout', 'yes', 'c', '10'], ['14', 'Amos', 'Daniel', 'yes', 'a', '5'], ['15', 'Caesar', 'Rivers', 'yes', 'b', '7'], ['16', 'Eugenia', 'Nichols', 'yes', 'b', '6'], ['17', 'dieter', 'alvarado', 'yes', 'b', '6'], ['18', 'Roary', 'Frank', 'yes', 'c', '7'], ['19', 'Ulric', 'Hensley', 'no', 'b', '9'], ['20', 'Felicia', 'Wilkins', 'yes', 'b', '8']]

def test_remove_empty_lines():
     #Arrange
    test_array = [[4,"Harding","Estrada","no",14],["","","","",],
                  [6,"Abra","Sheppard","yes",6],[6,"Abra","Sheppard","no",8]]
    #Act
    array_deduped = remove_duplicates(test_array)
    array_clean = remove_empty_lines(array_deduped)
    #Assert
    assert array_clean == [[4,"Harding","Estrada","no",14],
                  [6,"Abra","Sheppard","yes",6]]

# Ticket 4

def test_capitalize_names():
    # Arrange (Define input data)
    headers = ['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3']
    data = [
        [1, 'john', 'doe', 'yes', 'no', 'yes'],
        [2, 'jane', 'smith', 'no', 'yes', 'no'],
    ]

    # Act (Apply the function to the data)
    result = capitalize_names(headers, data)

    # Assert (Check if the first_name and last_name fields are capitalized)
    for entry in result:
        assert entry[headers.index('first_name')] == entry[headers.index('first_name')].capitalize()
        assert entry[headers.index('last_name')] == entry[headers.index('last_name')].capitalize()

# Ticket 5

def test_validate_answer_3():
    # Arrange (Define input data)
    data = [
        [1, 'John', 'Doe', 'yes', 'no', 5],
        [2, 'Jane', 'Smith', 'no', 'yes', 12],
        [3, 'Alice', 'Johnson', 'yes', 'yes', 'invalid'],
        [4, 'Bob', 'Brown', 'no', 'no', 8],
    ]

    # Act (Apply the function to the data)
    result = validate_answer_3(data)

    # Assert (Check if the result contains only valid rows)
    for entry in result:
        assert 1 <= entry[5] <= 10  # Directly access 'answer_3' by index (assuming it's at index 5)

# Ticket 6

def test_output_exists():
    # arrange
    in_file = "results.csv"
    out_file = "results_output_test.csv"
    # act
    in_data = get_input(in_file)
    output_to_file(out_file,in_data)
    out_data = get_input(out_file)
    # assert
    assert out_data == in_data