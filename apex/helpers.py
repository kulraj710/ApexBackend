import re

def validate_is_date(date_string):
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$", re.IGNORECASE)
    if pattern.match(date_string):
        return True
    else:
        return False