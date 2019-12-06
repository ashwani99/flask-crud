import re

def is_mobile_number_valid(number):
    """ Utility function to validate a mobile number using regular expression """
    mobile_number_re = re.compile(r"^[6-9]\d{9}$")
    return mobile_number_re.match(number) is not None