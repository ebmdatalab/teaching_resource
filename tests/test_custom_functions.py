from code.custom_functions import sum_values

def test_sum_values():
    values= [1, 2, 3]
    
    tested_sum = sum_values(values)
    
    unit_test_sum = 0
    for number in values:
        unit_test_sum = unit_test_sum + number
    
    assert tested_sum == unit_test_sum, "function output does not match expected value"

