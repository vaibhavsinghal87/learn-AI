# function that takes either celisus or fahrenheit and converts it to the other
def convert_temp(temp, scale):
    if scale == 'C':
        return (temp * 9/5) + 32
    elif scale == 'F':
        return (temp - 32) * 5/9
    else:
        raise ValueError("Scale must be either 'C' or 'F'")