import re

def valid_number(phone_number):
    model = re.compile('([0-9]){2} ([0-9]){5}([0-9]){4}')
    valid = model.search(phone_number)
    return valid

def valid_zip_code(zip_code):
    model = re.compile("[0-9]{5}[-]?[0-9]{3}")
    valid = model.search(zip_code)
    return valid

