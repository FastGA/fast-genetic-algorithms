"""
A few utilitary functions.
"""


def flip(array, i):
    """
    'array' should be an indexable object holding only 0s and 1s.
    This function flips the i-th value in 'array' : if it is 0, it becomes 1, and vice-versa.
    """
    array[i] ^= 1


def wrong_param_error(value, supported_values=None):
    """
    Returns a nicely-formatted error when a given parameter is not of valid value for some function.
    """
    string = "Wrong parameter value '{}'".format(value)
    if supported_values is not None:
        string += (" ; expected values are {{{}}}"
                   .format(", ".join(["{}".format(supported) for supported in supported_values])))
    return ValueError(string + ".")

