import re

def check_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return bool(re.match(pattern, email))

def extract_numbers(text):
    return re.findall(r"\d+", text)

def check_phone(phone):
    pattern = r"^\+7\d{10}$"
    return bool(re.fullmatch(pattern, phone))