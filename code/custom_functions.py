'''Custom functions for my project'''

def multiplier(number1, number2):
    ''' Function that takes in two values and returns a rounded multiple'''
    result = number1 * number2
    return round(result, 1)

def calbmi(height, weight):
    '''function that takes in height and weight and
    calculates a BMI to nearest 1 dp
    
    Args:
        height (float): Height in inches
        weight (float): Weight in inches
        
    Returns:
        bmi (float): Rounded to 1 decimal point
        
    '''   
    bmi = round(weight/(height**2), 1)
    return bmi

def sum_values(number_list):
    '''take in 3 values and returns a sum of these values'''
    return sum(number_list)