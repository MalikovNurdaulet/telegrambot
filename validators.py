import re

def check_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return bool(re.match(pattern, email))

def extract_numbers(text):
    return re.findall(r"\d+", text)