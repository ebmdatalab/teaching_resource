'''Custom functions for my project'''

def multiplier(number1, number2):
    ''' Function that takes in two values and returns a rounded multiple'''
    result = number1 * number2
    return round(result, 1)

def calbmi(height, weight):
    """
    Function that takes in height and weight and
    calculates a BMI to nearest 1 dp
    
    Args:
        height (float): Height in metres
        weight (float): Weight in kilos
        
    Returns:
        bmi (float): Rounded to 1 decimal point

    Raises:
    	ValueError: if height or weight unrealistic
        
    """
    if height < 1 or height > 2.2:
    	raise ValueError("Height either <1 metre or >2.2 metres. Please check input")
    elif weight < 35 or weight > 300:
    	raise ValueError("Weight either <35kg or >300kgs. Please check input")
    else:
	    bmi = round(weight/(height**2), 1)
	    return bmi

def sum_values(number_list):
    '''take in 3 values and returns a sum of these values'''
    return sum(number_list)
