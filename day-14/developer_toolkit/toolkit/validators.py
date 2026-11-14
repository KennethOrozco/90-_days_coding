def is_valid_age(age: int) -> bool:
    if age >= 0 and age <= 120:
        return True
    return False

def is_valid_email(email: str) -> bool:
    if email.count("@") == 1:
        valid = email.split("@")
        if valid[1].count(".") == 1:
            domain_parts = valid[1].split(".")
            if valid[0].strip() and domain_parts[0].strip() and domain_parts[1].strip():
                return True
    return False

